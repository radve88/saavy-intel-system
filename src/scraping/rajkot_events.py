import requests
from bs4 import BeautifulSoup

def scrape_rajkot_events():
    url = "https://www.gujarattourism.com/events.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    events = []
    for item in soup.select(".event-card"):
        title = item.select_one("h3").text.strip()
        date = item.select_one(".event-date").text.strip()
        events.append({"title": title, "date": date})

    return events
