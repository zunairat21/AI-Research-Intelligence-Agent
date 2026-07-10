from bs4 import BeautifulSoup

with open("data/sample_news.html", "r") as file:
    html = .read()

parsed_updates = []

soup = BeautifulSoup(html, "html.parser")

cards = soup.find_all("div", class_ = "news-card")

for card in cards:
    title = card.find("h2").get_text()
    category = card.find("p", class_ ="category").get_text()
    summary = card.find("p", class_  = "summary").get_text()
    date = card.find("time").get_text()
    url = card.find("a").get("href")

    parsed_updates.append(
       { "title": title,
        "category":category,
        "summary":summary,
        "date": date,
        "url":url
       }
    )
print( parsed_updates)
