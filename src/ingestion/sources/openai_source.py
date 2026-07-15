from src.ingestion.models import AIUpdate
from typing import List,Dict,Any
import requests
from bs4 import BeautifulSoup
class OpenAISource:
    BASE_URL = "https://openai.com/news/"
    """
        Collect AI updates from OpenAI
    """
    def fetch_raw_data(self) -> Any:
    
        raw_response = requests.get(
            self.BASE_URL,
            timeout=20)
        if raw_response.status_code == 200:
            return raw_response
        
        raise Exception(
            f"Failed to fetch openAI due to status code:{raw_response.status_code}"
            )
        
    
    def parse_response(self, raw_response) -> List[Dict[str,Any]]:

        html = raw_response.text
        soup = BeautifulSoup(html, "html.parser")
        parsed_updates = []
        cards = soup.select("div.group.relative")
        for card in cards:

            article = card.find("a")
            if article is None:
                continue

            title_element = article.find("div", class_="mb-4 text-h5 @md:pe-8")
            if title_element is None:
                print("="*50)
                print(article.prettify())
                continue
            title = title_element.get_text(strip=True)
            category = article.find("span").get_text()
            url =article.get("href")
            date= article.find("time").get_text()
            parsed_updates.append(
            {
                "title" :title,
                "category" : category,
                "url":url,
                "date":date
            }
        )
        return parsed_updates

        
    
    def convert_to_ai_updates(self, parsed_updates) -> List[AIUpdate]:
        """
           Convert the parsed dictionaries into AIUpdate objects.
        """
        ai_updates = []

        for update in parsed_updates:
            ai_update = AIUpdate(
                title=update["title"],
                source="OpenAI",
                url=update["url"],
                date=update["date"],
                category=update["category"]
                
            )

            ai_updates.append(ai_update)

        return ai_updates
    