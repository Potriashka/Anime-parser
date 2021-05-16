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

print("0 - all animes\n\nThen genres:\n\n" + "1 - dementia\n\n2 - martial arts\n\n3 - vampire\n\n\
4 - military\n\n5 - harem\n\n6 - demons\n\n7 - mystery\n\n8 - kids\n-----------------" if russian else \
"1 - action adventure\n\n2 - comedy\n\n3 - drama\n\n\
4 - fantasy\n\n5 - horror\n\n6 - kids family\n\n7 - lgbt\n\n8 - live action\n\n9 - mystery thriller\n\n10 - romance\n\n\
11 - science-fiction\n\n12 - sports\n\n13 - supernatural\n-----------------")

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
    url = 'https://www.google.com/search?q=' + item.text + ' смотреть ' + '&aqs=chrome..69i57.8359j0j1&sourceid=chrome&ie=UTF-8' if russian else 'https://www.google.com/search?q=' + item.text + " watch " + '&aqs=chrome..69i57.8359j0j1&sourceid=chrome&ie=UTF-8'

    req = requests.get(url, headers=headers)
    src = req.text

    with open("index.html", "w") as file:
        file.write(src)

    with open("index.html") as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")
    link = soup.find("div", class_="yuRUbf").find('a')
    link = link.get("href")
    print(item.text, " " + link + "\n")
