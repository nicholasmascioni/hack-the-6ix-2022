
from bs4 import BeautifulSoup
import requests

html_text = requests.get("https://www.nofrills.ca/search?search-bar=banana").text
soup = BeautifulSoup(html_text, 'lxml')

something = soup.find_all('div')
print(something)

