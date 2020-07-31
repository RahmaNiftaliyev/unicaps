# -*- coding: UTF-8 -*-
"""
Test data
"""

import base64
import os.path
import pathlib
from unittest import mock

from unicaps import CaptchaSolvingService, exceptions as exc
from unicaps.captcha import (
    CaptchaType, ImageCaptcha, RecaptchaV2, RecaptchaV3, FunCaptcha
)
from unicaps.common import CaptchaAlphabet, CaptchaCharType, WorkerLanguage

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

API_KEY = 'test'

IMAGE_FILE_PATH = os.path.join(CURRENT_DIR, 'image.jpg')
IMAGE_FILE_PATHLIB = pathlib.Path(IMAGE_FILE_PATH)
IMAGE_FILE_FILEOBJECT = open(IMAGE_FILE_PATH, 'rb')
IMAGE_FILE_BYTES = open(IMAGE_FILE_PATH, 'rb').read()
IMAGE_FILE_BASE64 = base64.b64encode(IMAGE_FILE_BYTES)
IMAGE_FILE_BASE64_STR = IMAGE_FILE_BASE64.decode('ascii')


INPUT_TEST_DATA_FOR_TASK_PREPARE_FUNC = {
    1: (ImageCaptcha(IMAGE_FILE_BYTES), None, None, None),
    2: (ImageCaptcha(IMAGE_FILE_PATHLIB), None, None, None),
    3: (ImageCaptcha(IMAGE_FILE_FILEOBJECT, is_phrase=True), None, None, None),
    4: (ImageCaptcha(IMAGE_FILE_BYTES, is_case_sensitive=True), None, None, None),
    5: (ImageCaptcha(IMAGE_FILE_BYTES, char_type=CaptchaCharType.ALPHA), None, None, None),
    6: (ImageCaptcha(IMAGE_FILE_BYTES, is_math=True), None, None, None),
    7: (ImageCaptcha(IMAGE_FILE_BYTES, min_len=1), None, None, None),
    8: (ImageCaptcha(IMAGE_FILE_BYTES, max_len=10), None, None, None),
    9: (ImageCaptcha(IMAGE_FILE_BYTES, alphabet=CaptchaAlphabet.LATIN), None, None, None),
    10: (ImageCaptcha(IMAGE_FILE_BYTES, language=WorkerLanguage.ENGLISH), None, None, None),
    11: (ImageCaptcha(IMAGE_FILE_BYTES, comment='test'), None, None, None),
    12: (RecaptchaV2('test1', 'test2'), None, None, None),
    13: (RecaptchaV2('test1', 'test2', is_invisible=True), None, None, None),
    14: (RecaptchaV2('test1', 'test2', data_s='test3'), None, None, None),
    15: (RecaptchaV3('test1', 'test2'), None, None, None),
    16: (RecaptchaV3('test1', 'test2', action='test3'), None, None, None),
    17: (RecaptchaV3('test1', 'test2', min_score=0.9), None, None, None),
    18: (FunCaptcha('test1', 'test2'), None, None, None),
    19: (FunCaptcha('test1', 'test2', service_url='test3'), None, None, None),
    20: (FunCaptcha('test1', 'test2', no_js=True), None, None, None),
}

BASE_TASK_REQUEST_DATA = {
    CaptchaSolvingService.TWOCAPTCHA: dict(
        method='POST',
        url='https://2captcha.com/in.php',
        headers={'Accept': 'application/json', 'Content-Type': 'application/json'},
        data=dict(key=API_KEY, json=1, soft_id=2738)
    ),
    CaptchaSolvingService.RUCAPTCHA: dict(
        method='POST',
        url='https://rucaptcha.com/in.php',
        headers={'Accept': 'application/json', 'Content-Type': 'application/json'},
        data=dict(key=API_KEY, json=1, soft_id=2738)
    ),
    CaptchaSolvingService.ANTI_CAPTCHA: dict(
        method='POST',
        json=dict(clientKey=API_KEY, softId=940),
        headers={'Accept': 'application/json', 'Content-Type': 'application/json'},
        url='https://api.anti-captcha.com/createTask'
    ),
}

OUTPUT_TEST_DATA_FOR_TASK_PREPARE_FUNC = {
    CaptchaSolvingService.TWOCAPTCHA: {
        1: {'data': dict(method='base64', body=IMAGE_FILE_BASE64)},
        2: {'data': dict(method='base64', body=IMAGE_FILE_BASE64)},
        3: {'data': dict(method='base64', body=IMAGE_FILE_BASE64, phrase=1)},
        4: {'data': dict(method='base64', body=IMAGE_FILE_BASE64, regsense=1)},
        5: {'data': dict(method='base64', body=IMAGE_FILE_BASE64, numeric=2)},
        6: {'data': dict(method='base64', body=IMAGE_FILE_BASE64, calc=1)},
        7: {'data': dict(method='base64', body=IMAGE_FILE_BASE64, min_len=1)},
        8: {'data': dict(method='base64', body=IMAGE_FILE_BASE64, max_len=10)},
        9: {'data': dict(method='base64', body=IMAGE_FILE_BASE64, language=2)},
        10: {'data': dict(method='base64', body=IMAGE_FILE_BASE64, lang='en')},
        11: {'data': dict(method='base64', body=IMAGE_FILE_BASE64, textinstructions='test')},
        12: {'data': dict(method='userrecaptcha', googlekey='test1', pageurl='test2', invisible=0)},
        13: {'data': dict(method='userrecaptcha', googlekey='test1', pageurl='test2', invisible=1)},
        14: {'data': {'method': 'userrecaptcha', 'googlekey': 'test1', 'pageurl': 'test2',
                      'invisible': 0, 'data-s': 'test3'}},
        15: {'data': dict(method='userrecaptcha', version='v3', googlekey='test1',
                          pageurl='test2')},
        16: {'data': dict(method='userrecaptcha', version='v3', googlekey='test1', pageurl='test2',
                          action='test3')},
        17: {'data': dict(method='userrecaptcha', version='v3', googlekey='test1', pageurl='test2',
                          min_score=0.9)},
        18: {'data': dict(method='funcaptcha', publickey='test1', pageurl='test2')},
        19: {'data': dict(method='funcaptcha', publickey='test1', pageurl='test2', surl='test3')},
        20: {'data': dict(method='funcaptcha', publickey='test1', pageurl='test2', nojs=1)},
    },
    CaptchaSolvingService.ANTI_CAPTCHA: {
        1: {'json': dict(task=dict(type='ImageToTextTask', body=IMAGE_FILE_BASE64_STR))},
        2: {'json': dict(task=dict(type='ImageToTextTask', body=IMAGE_FILE_BASE64_STR))},
        3: {'json': dict(task=dict(type='ImageToTextTask', body=IMAGE_FILE_BASE64_STR,
                                   phrase=True))},
        4: {'json': dict(task=dict(type='ImageToTextTask', body=IMAGE_FILE_BASE64_STR, case=True))},
        5: {'json': dict(task=dict(type='ImageToTextTask', body=IMAGE_FILE_BASE64_STR, numeric=2))},
        6: {'json': dict(task=dict(type='ImageToTextTask', body=IMAGE_FILE_BASE64_STR, math=True))},
        7: {'json': dict(task=dict(type='ImageToTextTask', body=IMAGE_FILE_BASE64_STR,
                                   minLength=1))},
        8: {'json': dict(task=dict(type='ImageToTextTask', body=IMAGE_FILE_BASE64_STR,
                                   maxLength=10))},
        9: {'json': dict(task=dict(type='ImageToTextTask', body=IMAGE_FILE_BASE64_STR))},
        10: {'json': dict(task=dict(type='ImageToTextTask', body=IMAGE_FILE_BASE64_STR),
                          languagePool='en')},
        11: {'json': dict(task=dict(type='ImageToTextTask', body=IMAGE_FILE_BASE64_STR,
                                    comment='test'))},
        12: {'json': dict(task=dict(type='NoCaptchaTaskProxyless', websiteKey='test1',
                                    websiteURL='test2', isInvisible=False))},
        13: {'json': dict(task=dict(type='NoCaptchaTaskProxyless', websiteKey='test1',
                                    websiteURL='test2', isInvisible=True))},
        14: {'json': dict(task=dict(type='NoCaptchaTaskProxyless', websiteKey='test1',
                                    websiteURL='test2', isInvisible=False,
                                    recaptchaDataSValue='test3'))},
        15: {'json': dict(task=dict(type='RecaptchaV3TaskProxyless', websiteKey='test1',
                                    websiteURL='test2'))},
        16: {'json': dict(task=dict(type='RecaptchaV3TaskProxyless', websiteKey='test1',
                                    websiteURL='test2', pageAction='test3'))},
        17: {'json': dict(task=dict(type='RecaptchaV3TaskProxyless', websiteKey='test1',
                                    websiteURL='test2', minScore=0.9))},
        18: {'json': dict(task=dict(type='FunCaptchaTaskProxyless', websitePublicKey='test1',
                                    websiteURL='test2'))},
        19: {'json': dict(task=dict(type='FunCaptchaTaskProxyless', websitePublicKey='test1',
                                    websiteURL='test2', funcaptchaApiJSSubdomain='test3'))},
        20: {'json': dict(task=dict(type='FunCaptchaTaskProxyless', websitePublicKey='test1',
                                    websiteURL='test2'))},
    }
}
OUTPUT_TEST_DATA_FOR_TASK_PREPARE_FUNC[CaptchaSolvingService.RUCAPTCHA] = (
    OUTPUT_TEST_DATA_FOR_TASK_PREPARE_FUNC[CaptchaSolvingService.TWOCAPTCHA]
)


def get_http_resp_obj(ret_value):
    obj = mock.Mock()
    obj.json = lambda: ret_value.copy()
    return obj


INPUT_TEST_LIST_FOR_TASK_PARSE_RESPONSE_FUNC = {
    1: CaptchaType.IMAGE,
    2: CaptchaType.RECAPTCHAV2,
    3: CaptchaType.RECAPTCHAV3,
    4: CaptchaType.TEXT
}

INPUT_TEST_DATA_FOR_TASK_PARSE_RESPONSE_FUNC = {
    CaptchaSolvingService.TWOCAPTCHA: {
        1: get_http_resp_obj(dict(status=1, request='1234567890')),
        2: get_http_resp_obj(dict(status=1, request='1234567890')),
        3: get_http_resp_obj(dict(status=1, request='1234567890')),
        4: get_http_resp_obj(dict(status=1, request='1234567890')),
    },
    CaptchaSolvingService.ANTI_CAPTCHA: {
        1: get_http_resp_obj(dict(errorId=0, taskId='1234567890')),
        2: get_http_resp_obj(dict(errorId=0, taskId='1234567890')),
        3: get_http_resp_obj(dict(errorId=0, taskId='1234567890')),
        4: get_http_resp_obj(dict(errorId=0, taskId='1234567890')),
    }
}
INPUT_TEST_DATA_FOR_TASK_PARSE_RESPONSE_FUNC[CaptchaSolvingService.RUCAPTCHA] = (
    INPUT_TEST_DATA_FOR_TASK_PARSE_RESPONSE_FUNC[CaptchaSolvingService.TWOCAPTCHA]
)

OUTPUT_TEST_DATA_FOR_TASK_PARSE_RESPONSE_FUNC = {
    CaptchaSolvingService.TWOCAPTCHA: {
        1: dict(task_id='1234567890', extra={}),
        2: dict(task_id='1234567890', extra={}),
        3: dict(task_id='1234567890', extra={}),
        4: dict(task_id='1234567890', extra={}),
    },
    CaptchaSolvingService.ANTI_CAPTCHA: {
        1: dict(task_id='1234567890', extra={}),
        2: dict(task_id='1234567890', extra={}),
        3: dict(task_id='1234567890', extra={}),
        4: None
    }
}
OUTPUT_TEST_DATA_FOR_TASK_PARSE_RESPONSE_FUNC[CaptchaSolvingService.RUCAPTCHA] = (
    OUTPUT_TEST_DATA_FOR_TASK_PARSE_RESPONSE_FUNC[CaptchaSolvingService.TWOCAPTCHA]
)

INPUT_TEST_DATA_FOR_TASK_PARSE_RESPONSE_FUNC_WITH_EXC = {
    CaptchaSolvingService.TWOCAPTCHA: {
        1: get_http_resp_obj(dict(status=0, request='ERROR_WRONG_USER_KEY')),
        2: get_http_resp_obj(dict(status=0, request='ERROR_KEY_DOES_NOT_EXIST')),
        3: get_http_resp_obj(dict(status=0, request='ERROR_ZERO_BALANCE')),
        4: get_http_resp_obj(dict(status=0, request='ERROR_NO_SLOT_AVAILABLE')),
    },
    CaptchaSolvingService.ANTI_CAPTCHA: {
        1: get_http_resp_obj(dict(errorId=1, errorCode='ERROR_WRONG_USER_KEY')),
        2: get_http_resp_obj(dict(errorId=2, errorCode='ERROR_KEY_DOES_NOT_EXIST')),
        3: get_http_resp_obj(dict(errorId=3, errorCode='ERROR_ZERO_BALANCE')),
        4: get_http_resp_obj(dict(errorId=4, errorCode='ERROR_NO_SLOT_AVAILABLE')),
    }
}
INPUT_TEST_DATA_FOR_TASK_PARSE_RESPONSE_FUNC_WITH_EXC[CaptchaSolvingService.RUCAPTCHA] = (
    INPUT_TEST_DATA_FOR_TASK_PARSE_RESPONSE_FUNC_WITH_EXC[CaptchaSolvingService.TWOCAPTCHA]
)

OUTPUT_TEST_DATA_FOR_TASK_PARSE_RESPONSE_FUNC_WITH_EXC = {
    CaptchaSolvingService.TWOCAPTCHA: {
        1: exc.AccessDeniedError,
        2: exc.AccessDeniedError,
        3: exc.LowBalanceError,
        4: exc.ServiceTooBusy,
    },
    CaptchaSolvingService.ANTI_CAPTCHA: {
        1: exc.AccessDeniedError,
        2: exc.AccessDeniedError,
        3: exc.LowBalanceError,
        4: exc.ServiceTooBusy,
    }
}
OUTPUT_TEST_DATA_FOR_TASK_PARSE_RESPONSE_FUNC_WITH_EXC[CaptchaSolvingService.RUCAPTCHA] = (
    OUTPUT_TEST_DATA_FOR_TASK_PARSE_RESPONSE_FUNC_WITH_EXC[CaptchaSolvingService.TWOCAPTCHA]
)
