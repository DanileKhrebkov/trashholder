from bs4 import BeautifulSoup
import requests
url = "https://ria.ru/economy/"
page = requests.get(url)

print(page.status_code)
filteredNews = []
allNews = []
soup = BeautifulSoup(page.text, "html.parser")
title_tag = soup.find("h1")
print(title_tag.text)