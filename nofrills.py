import requests
from bs4 import BeautifulSoup

URL = "https://www.nofrills.ca/search?search-bar=bananas"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

res = soup.title

print(res.get_text())   