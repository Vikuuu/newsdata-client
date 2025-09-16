from newsdata_client import NewsDataClient


def main():
    client = NewsDataClient(api_key="pub_XXXX")

    try:
        latest_json = client.latest(
            category=["technology"],
            language=["en"],
            full_content=True,
        )
    except Exception as e:
        print("Error while getting latest data ", e)


if __name__ == "__main__":
    main()
