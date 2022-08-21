import requests
from bs4 import BeautifulSoup

#-------------------------------------------------------------------------------------------------------------------------#

# First try did not really work

# URL = "https://www.nofrills.ca/search?search-bar=bananas"
# page = requests.get(URL)

# soup = BeautifulSoup(page.content, "html.parser")

# results = soup.find(class_ = "responsive-image")

# food_elements = results.find_all(class_= "Bananas, Bunch")

# for food in food_elements:
#     groceries = results.find_all(
#     "h2", string=lambda text: "banana" in text.lower()
#     )

#     groceries_elements = [
#         h2_element.parent.parent.parent for h2_element in groceries
#     ]
# for job_element in groceries_elements:
#     # -- snip --
#     links = job_element.find_all("a")
#     for link in links:
#         link_url = job_element.find_all("a")[1]["href"]
#         print(f"Apply here: {link_url}\n")

# foods = [a.find('img') for a in soup.find_all("a", {"class": "product-tile__thumbnail"}) if a.find('img')]
# name = [foods.get('alt') for food in foods]

# print(name)

# foods = [a.find('img').get('alt') for a in soup.find_all("a", {"class": "product-tile__thumbnail"}) if a.find('img')]

# print(foods)

# -------------------------------------------------------------------------------------------------------------------------#

# Second try!

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

headers = {'User-Agent': user_agent, }

url = 'https://www.nofrills.ca/search?search-bar=bananas'

request = urllib.request.Request(url, None, headers)

response = urllib.request.urlopen(request)

soup = BeautifulSoup(response, 'html.parser')

for foo in soup.find_all('img', alt=True):

    print(foo['alt'])

# -------------------------------------------------------------------------------------------------------------------------#

# Third try! following tutorial



