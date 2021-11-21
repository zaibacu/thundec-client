import logging

import requests

from typing import List, Optional

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

    @property
    def categories(self):
        resp = self.client.get(self.url + "/categories/", headers=self.headers)
        if resp.status_code == 200:
            return resp.json()
        return resp

    @property
    def flags(self):
        resp = self.client.get(self.url + "/flags/", headers=self.headers)
        if resp.status_code == 200:
            return resp.json()
        return resp

    def add_product(self, product_id: str, stock_level: int, categories: Optional[List[str]] = None, flags: Optional[List[str]] = None):
        data = {
            "product_id": product_id,
            "state": 0,
            "categories": list(map(lambda x: {"key": x}, categories)) if categories else [],
            "flags": list(map(lambda x: {"title": x}, flags)) if flags else [],
            "stock_level": {"level": stock_level}
        }
        resp = self.client.post(self.url + "/products/", headers=self.headers, json=data)
        if resp.status_code == 200:
            return resp.json()
        return resp
