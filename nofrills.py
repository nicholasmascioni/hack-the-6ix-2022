import requests
from bs4 import BeautifulSoup

URL = "https://www.nofrills.ca/search?search-bar=bananas"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find("div", class_ = "search-page__result")

food_elements = results.find_all("div", class_= "product-tracking")

for food in food_elements:
    groceries = results.find_all(
    "h2", string=lambda text: "banana" in text.lower()
    )

    groceries_elements = [
        h2_element.parent.parent.parent for h2_element in groceries
    ]
for job_element in groceries_elements:
    # -- snip --
    links = job_element.find_all("a")
    for link in links:
        link_url = job_element.find_all("a")[1]["href"]
        print(f"Apply here: {link_url}\n")