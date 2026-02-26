import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

# this ol is the container of all the content
response = soup.find('ol', class_="row")
if response:
    item_cards = response.find_all("article", class_ = "product_pod")
    for item_card in item_cards[0:5]:
        link = item_card.select("div.image_container a")
        print(link)
else:
    item_cards = []


