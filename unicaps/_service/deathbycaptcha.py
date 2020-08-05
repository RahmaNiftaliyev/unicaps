# -*- coding: UTF-8 -*-
"""
deathbycaptcha.com service
"""

import json
from typing import Dict

from .base import SocketService
from .._transport.socket_transport import StandardSocketTransport, SocketRequestJSON  # type: ignore
from .. import exceptions
from ..__version__ import __version__ as VERSION


class DBCSocketTransport(StandardSocketTransport):
    """ DeathByCaptcha Socket Transport """

    SOCKET_HOST = 'api.dbcapi.me'  # type: ignore
    SOCKET_PORTS = tuple(range(8123, 8131))  # type: ignore

    def _log_in(self, authtoken):
        return self._make_request(
            dict(authtoken=authtoken,
                 cmd="login")
        )

    def _make_request(self, request_data: dict) -> dict:
        """ Make a request """

        # connect
        if not self._socket:
            self.connect()

        # log in
        if request_data.get('cmd') != 'login':
            self._log_in(request_data.pop('authtoken'))

        return self._sendrecv(json.dumps(request_data))


class Service(SocketService):
    """ Main service class for deathbycaptcha.com """

    def _init_transport(self):  # pylint: disable=no-self-use
        return DBCSocketTransport()

    def _post_init(self):
        """ Init settings """

        for captcha_type in self._settings:
            self._settings[captcha_type].polling_delay = 2
            self._settings[captcha_type].polling_interval = 2
            self._settings[captcha_type].solution_timeout = 180


class Request(SocketRequestJSON):
    """ Base Request class """

    def prepare(self) -> Dict:
        """ Prepare request """

        request = super().prepare()
        request.update(
            dict(
                authtoken=self._service.api_key,
                version=f"Unicaps/Python v{VERSION}"
            )
        )
        return request

    def parse_response(self, response) -> Dict:
        """ Parse response """

        response = super().parse_response(response)

        error_id = response.get('error')
        if not error_id:
            return response

        if error_id in ('not-logged-in', 'invalid-credentials'):
            raise exceptions.AccessDeniedError('Access denied, check your credentials')
        if error_id == 'banned':
            raise exceptions.AccessDeniedError('Access denied, account is suspended')
        if error_id == 'insufficient-funds':
            raise exceptions.LowBalanceError('CAPTCHA was rejected due to low balance')
        if error_id == 'invalid-captcha':
            raise exceptions.BadInputDataError('CAPTCHA is not valid')
        if error_id == 'service-overload':
            raise exceptions.ServiceTooBusy(
                'CAPTCHA was rejected due to service overload, try again later')

        raise exceptions.ServiceError(error_id)


class GetBalanceRequest(Request):
    """ GetBalance Request class """

    def prepare(self) -> Dict:
        request = super().prepare()
        request.update(dict(cmd="login"))
        return request

    def parse_response(self, response) -> dict:
        """ Parses response and returns balance """

        return {'balance': float(super().parse_response(response)['balance'])}


class GetStatusRequest(Request):
    """ GetStatus Request class """


class ReportGoodRequest(Request):
    """ ReportGood Request class """

    # pylint: disable=arguments-differ,unused-argument
    def prepare(self, solved_captcha) -> dict:  # type: ignore
        """ Prepare request """

        return super().prepare()


class ReportBadRequest(Request):
    """ ReportBad Request class """

    # pylint: disable=arguments-differ,unused-argument
    def prepare(self, solved_captcha) -> dict:  # type: ignore
        """ Prepare request """

        return super().prepare()


class TaskRequest(Request):
    """ Common Task Request class """

    def prepare(self) -> Dict:
        request = super().prepare()
        request.update(dict(cmd="upload"))
        return request

    def parse_response(self, response) -> dict:
        """ Parse response and return task_id """

        response_data = super().parse_response(response)

        return dict(
            task_id=response_data.pop("captcha"),
            extra=response_data
        )


class SolutionRequest(Request):
    """ Common Solution Request class """

    # pylint: disable=arguments-differ
    def prepare(self, task) -> dict:  # type: ignore
        """ Prepare request """

        request = super().prepare()
        request.update(
            dict(cmd='captcha',
                 captcha=task.task_id)
        )
        return request

    def parse_response(self, response) -> dict:
        """ Parse response and return solution and cost """

        response_data = super().parse_response(response)

        return dict(
            solution=response_data["text"],
            cost=None
        )


class RecaptchaV2TaskRequest(TaskRequest):
    """ reCAPTCHA v2 task request """

    # pylint: disable=arguments-differ,unused-argument
    def prepare(self, captcha, proxy, user_agent, cookies) -> dict:  # type: ignore
        """ Prepare request """

        request = super().prepare()
        request.update(
            dict(
                type=4,
                token_params=json.dumps(
                    dict(googlekey=captcha.site_key,
                         pageurl=captcha.page_url)
                )
            )
        )

        return request


class RecaptchaV2SolutionRequest(SolutionRequest):
    """ reCAPTCHA v2 solution request """
