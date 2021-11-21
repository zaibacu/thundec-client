import logging

import requests

logger = logging.getLogger(__name__)
DEFAULT_URL = "http://localhost:8000/api"


class Client(object):
    def __init__(self, auth_token, api_url=DEFAULT_URL, api_version="v1"):
        self.url = f"{api_url}/{api_version}"
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Token {auth_token}"
        }

        self.client = requests.Session()

    @property
    def products(self):
        resp = self.client.get(self.url + "/products/", headers=self.headers)
        if resp.status_code == 200:
            return resp.json()
        return resp