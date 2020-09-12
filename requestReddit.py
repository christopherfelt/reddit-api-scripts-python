import requests
from bs4 import BeautifulSoup
import re

html = requests.get("https://www.reddit.com/r/Music/wiki/musicsubreddits")

soup = BeautifulSoup(html.text, 'html.parser')
genre = soup.find("div", class_="_3kIjxjzGVq5UfR6Bjiovd")
# print(soup.html)
print(genre.prettify())

# genres = genre.find_all(re.compile('^h[1-6]$'))
# genres = soup.find('h1')
# print(genres)
newHtmlFile = open("index.txt", "w+")
newHtmlFile.write(str(genre.prettify().encode("utf-8")))
newHtmlFile.close()
