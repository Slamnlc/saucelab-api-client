import json
import os

import requests


class Session:
    def __init__(self, host: str, username: str, token: str):
        """
        https://docs.saucelabs.com/dev/api/
        Insert your api server
        :param host:
        :param username: your username
        :param token: tour API token
        """
        if host[-1] == '/':
            host = host[:-1]
        self.__host = host
        self._session = requests.Session()
        self._session.auth = (username, token)
        self._device_cache = os.path.join(os.path.dirname(__file__), 'devices.json')

    def request(self, method: str, url: str, data: dict = None, params: dict = None, **kwargs):
        data = json.dumps(data) if data else ''
        self._session.headers.pop('Content-Type') if 'download' in url else \
            self._session.headers.update({'Content-Type': 'application/json'})
        response = self._session.request(method=method, url=f'{self.__host}{url}', data=data, params=params, **kwargs)
        if response.status_code in (200, 201):
            return response.content if 'download' in url else response.json()
        else:
            return f'Error: {response.status_code}: {response.reason} ({response.text})'

    def __del__(self):
        if os.path.isfile(self._device_cache):
            os.remove(self._device_cache)
