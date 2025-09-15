import requests
import unittest
import os

from newsdata_client import NewsDataClient
from newsdata_client.newsdata_exception import NewsDataException
from dotenv import load_dotenv

load_dotenv()



class TestNewsDataClient(unittest.TestCase):
    def test_latest(self):
        client = get_newsdata_client()
        try:
            response = client.latest()
        except Exception as e:
            self.fail(e)

    def test_incorrect_api_url(self):
        client = get_newsdata_client()
        client.latest_endpoint = client.latest_endpoint.replace("latest", "lat")

        self.assertRaises(NewsDataException, client.latest)

    def test_latest_with_q(self):
        client = get_newsdata_client()

        try:
            response = client.latest(q="social")
        except Exception as e:
            self.fail(e)

        try:
            response = client.latest(q="social pizza")
        except Exception as e:
            self.fail(e)

    def test_crpyto(self):
        client = get_newsdata_client()
        try:
            response = client.crypto()
        except Exception as e:
            self.fail(e)

    def test_crypto_with_param_coin(self):
        client = get_newsdata_client()
        try:
            response = client.crypto(coin=["btc", "bnb", "eth"])
        except Exception as e:
            self.fail(e)

    def test_crypto_with_param_lang(self):
        client = get_newsdata_client()
        try:
            response = client.crypto(language=["it", "en"])
        except Exception as e:
            self.fail(e)

    def test_crypto_with_param_domain_url(self):
        client = get_newsdata_client()
        try:
            response = client.crypto(domainur=["coindesk.com"])
        except Exception as e:
            self.fail(e)

    def test_archive(self):
        client = get_newsdata_client()
        self.assertRaises(NewsDataException, client.archive)

    def test_archive_with_param_category(self):
        client = get_newsdata_client()
        try:
            response = client.archive(category=["technology", "science"])
        except Exception as e:
            self.fail(e)

    def test_archive_with_param_from_to_date(self):
        client = get_newsdata_client()
        try:
            response = client.archive(
                from_date="2025-09-01", to_date="2025-09-14", category=["technology"]
            )
        except Exception as e:
            self.fail(e)

    def test_archive_with_param_from_date(self):
        client = get_newsdata_client()
        try:
            response = client.archive(from_date="2025-08-25", category=["science"])
        except Exception as e:
            self.fail(e)

    def test_sources(self):
        client = get_newsdata_client()
        try:
            response = client.sources()
        except Exception as e:
            self.fail(e)

    def test_sources_with_params_country(self):
        client = get_newsdata_client()
        try:
            response = client.sources(country=["ua"])
        except Exception as e:
            self.fail(e)

    def test_sources_with_params_category(self):
        client = get_newsdata_client()
        try:
            response = client.sources(category=["politics"])
        except Exception as e:
            self.fail(e)

    def test_sources_with_params_language(self):
        client = get_newsdata_client()
        try:
            response = client.sources(language=["nl"])
        except Exception as e:
            self.fail(e)


def get_newsdata_client() -> NewsDataClient:
    c = NewsDataClient(api_key=os.environ.get("API_KEY"))

    return c


if __name__ == "__main__":
    unittest.main()
