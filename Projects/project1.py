import requests
from bs4 import BeautifulSoup

import sys

url = sys.argv[1]
response = requests.get(url)

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")

title = soup.title.get_text()

print(title)

body_text = soup.get_text()

print(body_text)

links = soup.find_all("a")

for i in links:
    href = i.get("href")

    if href:
        print(href)