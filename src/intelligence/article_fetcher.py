import requests


class ArticleFetcher:

    def fetch(self, url: str) -> str:
        raw_response = requests.get(
            url,
            timeout=20
        )

        raw_response.raise_for_status()
        raw_response.encoding = raw_response.apparent_encoding

        return raw_response.text
