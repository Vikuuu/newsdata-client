import requests
from newsdata_client import NewsDataClient


def main():
    with requests.Session() as session:
        session_client = NewsDataClient(api_key="pub_XXXX", session=session)
        latest_json = session_client.latest()
        archive_json = session_client.archive(language=["en"])


if __name__ == "__main__":
    main()
