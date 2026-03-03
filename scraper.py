import requests
from bs4 import BeautifulSoup
import sys
 
url = sys.argv[1]


if not url.startswith("http"):
    url = "https://" + url

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")

if soup.title:
    print(soup.title.get_text().strip())
else:
    print("No title found")


body_text = soup.get_text(separator="\n")
lines = body_text.splitlines()


clean_lines = [line.strip() for line in lines if line.strip()]

for line in clean_lines:
    print(line)


links = soup.find_all("a")

for link in links:
    href = link.get("href")
    if href:
        print(href)