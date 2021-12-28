import time
import base64
import hmac
import hashlib


class SensCommon:
    def __init__(self):
        self._accessKeyId = 'se2VYxr28ke9B4bq9OBR'
        self._secretKey = 'jTMTIfVJUkFnbx79DAEaQ8NHb48divvTFreGbg7x'
        self._serviceId = 'ncp:sms:kr:259184051956:hs_notice'
        self._host = 'https://sens.apigw.ntruss.com'

    def _headers(self, method, uri):
        timestamp = str(int(time.time() * 1000))
        secretKey = bytes(self._secretKey, 'UTF-8')
        message = '{} {}\n{}\n{}'.format(method, uri, timestamp, self._accessKeyId)
        message = bytes(message, 'UTF-8')
        signingKey = base64.b64encode(hmac.new(secretKey, message, digestmod=hashlib.sha256).digest()).decode('UTF-8')
        return {
            'Content-Type': 'application/json; charset=utf-8',
            'x-ncp-apigw-timestamp': timestamp,
            'x-ncp-iam-access-key': self._accessKeyId,
            'x-ncp-apigw-signature-v2': signingKey
        }