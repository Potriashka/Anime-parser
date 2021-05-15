import requests
from bs4 import BeautifulSoup

headers = { # maybe we'll need it to avoid an anti-parser system //but maybe, if you have an error, you should delete it
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
}

urlsRU = ["https://animego.org/anime", "https://animego.org/anime/filter/genres-is-dementia/apply", "https://animego.org/anime/filter/genres-is-martial-arts/apply",
        "https://animego.org/anime/filter/genres-is-vampire/apply", "https://animego.org/anime/filter/genres-is-military/apply", "https://animego.org/anime/filter/genres-is-harem/apply",
        "https://animego.org/anime/filter/genres-is-demons/apply", "https://animego.org/anime/filter/genres-is-mystery/apply", "https://animego.org/anime/filter/genres-is-kids/apply"]

urlsEN = ["https://www.hidive.com/dubs", "https://www.hidive.com/dubs/action-adventure?sort=a-z&audio=all&subtitles=all", "https://www.hidive.com/dubs/comedy?sort=a-z&audio=all&subtitles=all",
          "https://www.hidive.com/dubs/drama?sort=a-z&audio=all&subtitles=all", "https://www.hidive.com/dubs/fantasy?sort=a-z&audio=all&subtitles=all", "https://www.hidive.com/dubs/horror?sort=a-z&audio=all&subtitles=all",
          "https://www.hidive.com/tv/kids-family?sort=a-z&audio=all&subtitles=all", "https://www.hidive.com/tv/lgbt?sort=a-z&audio=all&subtitles=all", "https://www.hidive.com/tv/live-action?sort=a-z&audio=all&subtitles=all",
          "https://www.hidive.com/tv/mystery-thriller?sort=a-z&audio=all&subtitles=all", "https://www.hidive.com/tv/romance?sort=a-z&audio=all&subtitles=all", "https://www.hidive.com/tv/science-fiction?sort=a-z&audio=all&subtitles=all",
          "https://www.hidive.com/tv/sports?sort=a-z&audio=all&subtitles=all", "https://www.hidive.com/tv/supernatural?sort=a-z&audio=all&subtitles=all"]

lang = input("Choose a language (en, ru):   ")

russian = lang == "ru"

print("0 - all animes\nThen genres:\n\n1 - dementia\n\n2 - martial arts\n\n3 - vampire\n\n4 - military\n\n5 - harem\n\n6 - demons\n\n7 - mystery\n\n8 - kids\n-----------------")

input = int(input())

print("-----------------")

url = urlsRU[input] if russian else urlsEN[input]

req = requests.get(url, headers=headers)
src = req.text

with open("index.html", "w") as file:
    file.write(src)

with open("index.html") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")

test = soup.findAll("div", class_="h5 font-weight-normal mb-1" if russian else "synopsis") # here we choose what we'll parse: anime names

for item in test:
    print(item.text + "\n")
