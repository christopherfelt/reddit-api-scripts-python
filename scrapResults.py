from bs4 import BeautifulSoup
import re

html = BeautifulSoup(open("index2.html"), "html.parser")

h2s = html.find_all("h2")
genre_text_file = open("genre.txt", "w+")

for el in h2s:
    el_str = el.text
    newstr = el_str.replace("\\n", "")
    genre_text_file.write(newstr.lstrip().rstrip()+", ")

genre_text_file.close()