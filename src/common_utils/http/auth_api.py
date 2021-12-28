from src.common_utils.http import HttpRequests
from src import settings

class AuthApi(HttpRequests):
    def __init__(self):
        super().__init__()
        self._api_server_url = ''
        self._env = settings.ENV
        if self._env == 'PROD':
            self._api_server_url = '{prod auth api url}'
        elif self._env == 'STAGE':
            self._api_server_url = '{stage auth api url}'
        elif self._env == 'DEV':
            self._api_server_url = '{dev auth api url}'
        else:
            self._api_server_url = 'http://127.0.0.1:11003'

    def check_access_key(self, access_token):
        body = {
            'token': access_token,
            'referer': 'nines',
            'tokenType': 'access'
        }
        res = self.post('/api/v1/authority/session/valid', {}, body)
        if not res:
            return {'result': False}
        return res.get('result')

