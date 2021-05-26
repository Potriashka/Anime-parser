import requests
from bs4 import BeautifulSoup

headers = { # maybe we'll need it to avoid an anti-parser system //but maybe, if you have an error, you should delete it
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
}

userInput = input("Enter a title:   ")
print("-----------------")

url = 'https://www.google.com/search?q=' + userInput + " watch " + '&aqs=chrome..69i57.8359j0j1&sourceid=chrome&ie=UTF-8'
urlSUB = 'https://www.google.com/search?q=' + userInput + " watch subtitles " + '&aqs=chrome..69i57.8359j0j1&sourceid=chrome&ie=UTF-8'

req = requests.get(url, headers=headers)
src = req.text

with open("index.html", "w") as file:
    file.write(src)

with open("index.html") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")
link = soup.find("div", class_="yuRUbf").find('a')
link = link.get("href")

req = requests.get(urlSUB, headers=headers)
src = req.text

with open("index.html", "w") as file:
    file.write(src)

with open("index.html") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")
linkSUB = soup.find("div", class_="yuRUbf").find('a')
linkSUB = linkSUB.get("href")

print(userInput + ":")
print(f"Watch:   {link}")
print(f"Watch with subtitles:   {linkSUB}")
