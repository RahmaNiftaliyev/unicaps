<p align="center"><img src="https://i.imgur.com/8aQf6On.png" /></p>

# Unicaps
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/unicaps.svg)](https://pypi.python.org/pypi/unicaps/)
[![PyPI version fury.io](https://badge.fury.io/py/unicaps.svg)](https://pypi.python.org/pypi/unicaps/)
[![PyPI status](https://img.shields.io/pypi/status/unicaps.svg)](https://pypi.python.org/pypi/unicaps/)
[![Build status](https://travis-ci.com/sergey-scat/unicaps.svg?branch=master)](https://travis-ci.com/github/sergey-scat/unicaps)
[![codecov](https://codecov.io/gh/sergey-scat/unicaps/branch/master/graph/badge.svg)](https://codecov.io/gh/sergey-scat/unicaps)
[![Documentation Status](https://readthedocs.org/projects/unicaps/badge/?version=latest)](https://unicaps.readthedocs.io/en/latest/?badge=latest)

Unicaps is a unified Python API for CAPTCHA solving services.


⚠ **PLEASE NOTE** </br>
⚠ A solving service API key is required to use this package!</br>
⚠ The list of the supported services you can find in the table below.


## Key Features
 - A unified Python interface that is independent of the service used
 - Uses native service protocol/endpoints (eg, no needs in patching _hosts_ file)
 - Supports 10 types of CAPTCHAs
 - Supports 5 CAPTCHA solving services (3 more would be added soon)
 - Written Pythonic way and is intended for humans

## Installation
```pip install unicaps```

## Simple Usage Example
```python
>>> from unicaps import CaptchaSolver
>>> solver = CaptchaSolver("2captcha.com", api_key="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
>>> solver.get_balance()
2.84161
>>> solved = solver.solve_image_captcha(open("captcha.jpg", "rb"), is_phrase=False, is_case_sensitive=True)
>>> solved.solution.text
'w93Bx'
>>> solved.cost
0.00078
>>> solved.report_good()
True
```

## Supported CAPTCHAs / Services
| CAPTCHA➡ \ Service⬇ | Image | Text | [reCAPTCHA v2](https://developers.google.com/recaptcha/docs/display) | [reCAPTCHA v3](https://developers.google.com/recaptcha/docs/v3) | [FunCaptcha](https://funcaptcha.com/fc/api/nojs/?pkey=69A21A01-CC7B-B9C6-0F9A-E7FA06677FFC) | [KeyCAPTCHA](https://www.keycaptcha.com/) | [Geetest](https://www.geetest.com/en/demo) | [hCaptcha](https://www.hcaptcha.com/) | [Capy](https://www.capy.me/) | TikTok
| ------------- | :---: | :---:	| :---:	| :---:	| :---:	| :---:	| :---:	| :---:	| :---:	| :---:	|
| [2captcha.com](http://2captcha.com/?from=8754088)	| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| [anti-captcha.com](http://getcaptchasolution.com/vus77mnl48) | ✅ | ❌ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ | ❌ |
| [azcaptcha.com](https://azcaptcha.com/) | ✅ | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| [cptch.net](https://cptch.net/auth/signup?frm=0ebc1ab34eb04f67ac320f020a8f709f) | ✅ | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| [deathbycaptcha.com](https://deathbycaptcha.com/) | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| [rucaptcha.com](https://rucaptcha.com?from=9863637) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

### reCAPTCHA v2
| Service | Regular | Invisible | Google service<sup>1</sup> | Proxy<sup>2</sup> | Cookies<sup>3</sup> | User-Agent<sup>4</sup> |
| ------------- | :---: | :---:	| :---:	| :---:	| :---:	| :---:	|
| [2captcha.com](http://2captcha.com/?from=8754088)	| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| [anti-captcha.com](http://getcaptchasolution.com/vus77mnl48) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| [azcaptcha.com](https://azcaptcha.com/) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| [cptch.net](https://cptch.net/auth/signup?frm=0ebc1ab34eb04f67ac320f020a8f709f) | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| [deathbycaptcha.com](https://deathbycaptcha.com/) | ✅ | ❌ | ✅ | ✅ | ❌ | ❌ |
| [rucaptcha.com](https://rucaptcha.com?from=9863637) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

<sup>1</sup> Support of reCAPTCHA on Google services (e.g. Google Search)
<sup>2</sup> Support of solving via proxy server
<sup>3</sup> Support of passing custom cookies
<sup>4</sup> Support of passing custom User-Agent header

## Supported CAPTCHAs / Services
| Service➡ \ CAPTCHA⬇ | [2captcha.com](http://2captcha.com/?from=8754088) | [anti-captcha.com](http://getcaptchasolution.com/vus77mnl48) | [azcaptcha.com](https://azcaptcha.com/) | [cptch.net](https://cptch.net/auth/signup?frm=0ebc1ab34eb04f67ac320f020a8f709f) | [deathbycaptcha.com](https://deathbycaptcha.com/) | [rucaptcha.com](https://rucaptcha.com?from=9863637) |
| ------------- | :---: | :---:	| :---:	| :---:	| :---:	| :---:	|
| Image CAPTCHA | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Text CAPTCHA | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ |
| [reCAPTCHA v2](https://developers.google.com/recaptcha/docs/display) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| [reCAPTCHA v3](https://developers.google.com/recaptcha/docs/v3) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| [FunCaptcha](https://funcaptcha.com/fc/api/nojs/?pkey=69A21A01-CC7B-B9C6-0F9A-E7FA06677FFC) | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ |
| [KeyCAPTCHA](https://www.keycaptcha.com/) | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ |
| [Geetest](https://www.geetest.com/en/demo) | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ |
| [hCaptcha](https://www.hcaptcha.com/) | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ |
| [Capy](https://www.capy.me/) | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ |
| TikTok | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ |



## Code examples
[Examples](https://github.com/sergey-scat/unicaps/tree/master/examples)
