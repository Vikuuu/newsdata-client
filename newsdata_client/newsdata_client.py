import requests

from newsdata_client.newsdata_auth import NewsDataAuth
from newsdata_client.newsdata_exception import NewsDataException


class NewsDataClient:
    def __init__(self, api_key):
        self.base_api_url = "https://newsdata.io/api/1/"
        self.latest_endpoint = f"{self.base_api_url}latest"
        self.crypto_endpoint = f"{self.base_api_url}crypto"
        self.archive_endpoint = f"{self.base_api_url}archive"
        self.sources_endpoint = f"{self.base_api_url}sources"

        self.auth = NewsDataAuth(api_key)
        self.request_method = requests

    def latest(self):
        response = self.request_method.get(self.latest_endpoint, auth=self.auth)

        if response.status_code != requests.codes.ok:
            if response.headers.get("content-type") == "application/json":
                raise NewsDataException(response.json())
            else:
                raise NewsDataException(str(response.content))

        return response.json()

    def crypto(self):
        response = self.request_method.get(self.crypto_endpoint, auth=self.auth)

        if response.status_code != requests.codes.ok:
            if response.headers.get("content-type") == "application/json":
                raise NewsDataException(response.json())
            else:
                raise NewsDataException(str(response.content))

        return response.json()

    def archive(self, category: str = "top"):
        payload = {}
        payload["category"] = category
        response = self.request_method.get(
            self.archive_endpoint, auth=self.auth, params=payload
        )

        if response.status_code != requests.codes.ok:
            if response.headers.get("content-type") == "application/json":
                raise NewsDataException(response.json())
            else:
                raise NewsDataException(str(response.content))

        return response.json()

    def sources(self):
        response = self.request_method.get(self.sources_endpoint, auth=self.auth)

        if response.status_code != requests.codes.ok:
            if response.headers.get("content-type") == "application/json":
                raise NewsDataException(response.json())
            else:
                raise NewsDataException(str(response.content))

        return response.json()
