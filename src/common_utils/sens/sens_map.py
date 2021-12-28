import requests
from . import SensCommon

class SensMap(SensCommon):
    def __init__(self):
        self._mapApiUrl = 'https://naveropenapi.apigw.ntruss.com'
        self._apiKeyId = '{api key id}'
        self._apiKey = '{api key}'

    def get_direction_15(self, start: str, goal: str, option: str = 'trafast'):
        request_uri = f"{self._mapApiUrl}/map-direction-15/v1/driving" \
                      f"?X-NCP-APIGW-API-KEY-ID={self._apiKeyId}&X-NCP-APIGW-API-KEY={self._apiKey}" \
                      f"&start={start}&goal={goal}&option={option}"
        response = requests.get(request_uri)
        return response.json()
