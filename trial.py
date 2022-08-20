import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome(executable_path='hack-the-6ix-2022/chromedriver.exe')
driver.get("https://www.nofrills.ca/search?search-bar=bananas")
results = []
content = driver.page_source
soup = BeautifulSoup(content)

for a in soup.findAll(attrs={'class': 'class'}):
    name = a.find('a')
    if name not in results:
        results.append(name.text)

for x in results:
   print(x)