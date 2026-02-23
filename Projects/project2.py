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



def word_to_number(word):
    total = 0
    for ch in word:
        total = total + ord(ch)
    return total


def make_simhash(counter):
    bucket = [0] * 64   # 64 empty boxes

    for word in counter:
        freq = counter[word]
        h = word_to_number(word)

        bit = 0
        while bit < 64:
            if (h >> bit) & 1 == 1:
                bucket[bit] = bucket[bit] + freq
            else:
                bucket[bit] = bucket[bit] - freq
            bit = bit + 1

    simhash = 0
    i = 0
    while i < 64:
        if bucket[i] >= 0:
            simhash = simhash | (1 << i)
        i = i + 1

    return simhash



def compare(a, b):
    both = a & b
    return bin(both).count("1")



url1 = sys.argv[1]
url2 = sys.argv[2]

text1 = download_page(url1)
text2 = download_page(url2)

words1 = get_words(text1)
words2 = get_words(text2)

count1 = make_count(words1)
count2 = make_count(words2)

simhash1 = make_simhash(count1)
simhash2 = make_simhash(count2)

same_bits = compare(simhash1, simhash2)

print("Simhash 1:", simhash1)
print("Simhash 2:", simhash2)
print("Common bits:", same_bits)
