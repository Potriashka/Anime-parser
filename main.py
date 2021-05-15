import requests
from bs4 import BeautifulSoup

headers = { # maybe we'll need it to avoid anti-parser system
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
}

urls = ["https://animego.org/anime", "https://animego.org/anime/filter/genres-is-dementia/apply", "https://animego.org/anime/filter/genres-is-martial-arts/apply",
        "https://animego.org/anime/filter/genres-is-vampire/apply", "https://animego.org/anime/filter/genres-is-military/apply", "https://animego.org/anime/filter/genres-is-harem/apply",
        "https://animego.org/anime/filter/genres-is-demons/apply", "https://animego.org/anime/filter/genres-is-mystery/apply", "https://animego.org/anime/filter/genres-is-kids/apply"]

print("0 - all animes\nThen genres:\n1 - dementia\n2-martial arts\n3-vampire\n4-military\n5-harem\n6-demons\n7-mystery\n8-kids")

input = input()

url = urls[int(input)]

req = requests.get(url, headers=headers)
src = req.text
# print(src)

with open("index.html", "w") as file:
    file.write(src)

with open("index.html") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")

test = soup.findAll("div", class_="h5 font-weight-normal mb-1") # here we choose what we'll parse: anime names

for item in test:
    print(item.text)
