import json

import requests as requests


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

    def request(self, method: str, url: str, data: dict = None, params: dict = None, **kwargs):
        data = json.dumps(data) if data else ''
        response = self._session.request(method=method, url=f"{self.__host}{url}", data=data, params=params, **kwargs)
        if response.status_code in (200, 201):
            return response.json()
        else:
            return f"Error: {response.status_code}: {response.reason}"
