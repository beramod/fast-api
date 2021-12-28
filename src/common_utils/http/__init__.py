import socket
import requests, json
from src.singeton import Singleton

class HttpRequests(Singleton):
    def __init__(self):
        self._api_server_url = None
        self._headers = {'Content-Type': 'application/json'}

    def get_ip_address(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]

    def get(self, uri, parameters):
        parameter = '&'.join(list(map(lambda key: '{}={}'.format(key, parameters.get(key)), parameters.keys())))
        try:
            response = requests.get('{}{}?{}'.format(self._api_server_url, uri, parameter), headers=self._headers)
            return response.json()
        except Exception as e:
            try:
                response = requests.get('{}{}?{}'.format(self._api_server_url, uri, parameter), headers=self._headers)
                return response.json()
            except Exception as e:
                return None

    def post(self, uri, parameters, body):
        parameter = ''

        for key in parameters:
            parameter = parameter + '&{}={}'.format(key, str(parameters.get(key)))
        try:
            response = requests.post('{}{}?{}'.format(self._api_server_url, uri, parameter), headers=self._headers,
                                    data=json.dumps(body))
            return response.json()
        except Exception as e:
            try:
                response = requests.post('{}{}?a{}'.format(self._api_server_url, uri, parameter), headers=self._headers,
                                         data=json.dumps(body))
                return response.json()
            except Exception as e:
                return None

    def put(self, uri, parameters, body):
        parameter = ''

        for key in parameters:
            parameter = parameter + '&{}={}'.format(key, str(parameters.get(key)))
        try:
            response = requests.put('{}{}?{}'.format(self._api_server_url, uri, parameter), headers=self._headers,
                                    data=json.dumps(body))
            return response.json()
        except Exception as e:
            try:
                response = requests.put('{}{}?{}'.format(self._api_server_url, uri, parameter), headers=self._headers,
                                        data=json.dumps(body))
                return response.json()
            except Exception as e:
                return None

    def delete(self, uri, parameters):
        parameter = ''

        for key in parameters:
            parameter = parameter + '&{}={}'.format(key, str(parameters.get(key)))
        try:
            response = requests.delete('{}{}?{}'.format(self._api_server_url, uri, parameter), headers=self._headers)
            return response.json()
        except Exception as e:
            try:
                response = requests.delete('{}{}?{}'.format(self._api_server_url, uri, parameter), headers=self._headers)
                return response.json()
            except Exception as e:
                return None
