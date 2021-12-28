from src.common_utils.http import HttpRequests
from src import settings

class FlowApi(HttpRequests):
    def __init__(self):
        super().__init__()
        self._api_server_url = ''
        self._env = settings.ENV
        if self._env == 'PROD':
            self._api_server_url = '{prod flow api ip}'
        else:
            self._api_server_url = '{dev flow api ip}'

    def run_flow(self, flow_name):
        res = self.get('/api/v1/flow-control/run', {'flow_name': flow_name})
        if not res:
            return {'result': False}
        return res.get('result')

    def run_flow_test(self, flow_name):
        res = self.get('/api/v1/flow-control/run/test', {'flow_name': flow_name})
        if not res:
            return {'result': False}
        return res.get('result')