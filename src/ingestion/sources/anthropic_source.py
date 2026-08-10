from src.ingestion.models import AIUpdate
from typing import List,Dict,Any
import requests
from bs4 import BeautifulSoup

class AnthropicSource:

    BASE_URL = "https://www.anthropic.com/news"

    def fetch_raw_data(self) ->Any:

        raw_response = requests.get(
            self.BASE_URL,
            timeout=20
        )

        if raw_response.status_code == 200:

            return raw_response

        raise Exception(f"Failed to fetch Anthrpoic due to status code:{raw_response.status_code}"
                        )

    def parse_response(self, raw_response) -> List[Dict[str,Any]]:

        html =raw_response.text
        soup = BeautifulSoup(html , "html.parser")
        parsed_updates = []
        cards = soup.find_all("li")

        for card in cards:

            article = card.find ("a")
            if article is None:
                continue

            meta = article.find("div")
            if meta is None:
                continue
            date_element = meta.find("time")
            if date_element is not None:
                date = date_element.get_text(strip=True)

            else:

                date = ""
            title_element= meta.find_next_sibling("span")
            if title_element is None:
                print("="*50)
                print(article.prettify())
                continue
            title = title_element.get_text(strip=True)
            url = article.get("href")


            if url is None:
                continue
            category_element = meta.find("span")

            if category_element is not None:
                category = category_element.get_text(strip=True)
            else:

                category = ""

            parsed_updates.append(
                {
                    "title" :title,
                    "url" : url,
                    "date" : date,
                    "category":category

                }
            )

        return parsed_updates

    def convert_to_ai_updates(self, parsed_updates) -> List[AIUpdate]:

        ai_updates =[]

        for update in parsed_updates:

            ai_update = AIUpdate(
                title=update["title"],
                source="Anthropic",
                url=update["url"],
                date = update["date"],
                category=update["category"],
                summary="",
                tags=""

            )
        
            ai_updates.append(ai_update)

        return ai_updates