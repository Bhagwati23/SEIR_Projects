import requests
from bs4 import BeautifulSoup
import sys

def download_page(url):
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text()
    return text


def get_words(text):
    text = text.lower()         
    words = text.split()         
    return words


def make_count(words):
    count = {}
    for w in words:
        if w in count:
            count[w] = count[w] + 1
        else:
            count[w] = 1
    return count



def common_words(c1, c2):
    common = 0
    for word in c1:
        if word in c2:
            common = common + 1
    return common



url1 = sys.argv[1]
url2 = sys.argv[2]

text1 = download_page(url1)
text2 = download_page(url2)

words1 = get_words(text1)
words2 = get_words(text2)

count1 = make_count(words1)
count2 = make_count(words2)

same = common_words(count1, count2)

print("Total unique words in page 1:", len(count1))
print("Total unique words in page 2:", len(count2))
print("Common words:", same)