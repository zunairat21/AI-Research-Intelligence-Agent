from src.ingestion.models import AIUpdate
from typing import List,Dict,Any
import requests
from bs4 import BeautifulSoup

class  DeepMindSource:

     BASE_URL = "https://deepmind.google/blog/"

     def fetch_raw_data(self) -> Any:

          raw_response = requests.get(
               self.BASE_URL,
               timeout=20
          )

          if raw_response.status_code == 200:

               return raw_response

          raise Exception(f"Failed to fetch DeepMind due to status code:{raw_response.status_code}")

     def parse_response(self, raw_response) -> List[Dict[str, Any]]:

            html = raw_response.text
            soup = BeautifulSoup(html, "html.parser")
            parsed_updates =[]
            cards = soup.find_all("article")

            for card in cards:

                  link_element = card.find("a")
                  if link_element is None:
                        continue

                  title_element = card.find("h3")
                  if title_element is  None:
                        print("="*50)
                        print(link_element.prettify())
                        continue

                  title = title_element.get_text(strip = True)

                  url = link_element.get("href") ##using get as href is attribute not a tag for tag we use find

                  if url is None:

                      continue

                  date_element  = card.find("time")

                  if date_element is not None:

                        date = date_element.get_text(strip=True)

                  else:
                        date = ""

                  category_element = card.find("span", class_="meta__category")

                  if category_element is not None:
                      category = category_element.get_text(strip=True)
                  else:

                     category = ""

                  parsed_updates.append(
                       
                        {
                             
                          "title" : title,
                          "source" : "DeepMind",
                           "url" : url,
                           "date" : date,
                           "category" : category
                    }

                  )

            return parsed_updates

     def convert_to_ai_updates(self, parsed_updates) -> List[AIUpdate]:

          ai_updates = []

          for update in parsed_updates:

               ai_update = AIUpdate(
                    title=update["title"],
                    source=update["source"],
                    url= update["url"],
                    date = update["date"],
                    category=update["category"],
                    summary ="",
                    tags = ""
               )

               ai_updates.append(ai_update)

          return ai_updates


                  

                  