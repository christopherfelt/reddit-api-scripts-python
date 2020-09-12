from bs4 import BeautifulSoup
import re
import json


def app():
    html = BeautifulSoup(open("index3.html"), "html.parser")

    h2s = html.find_all("h2")
    # genre_text_file = open("genre.txt", "w+")
    genre_dict = {}
    for el in h2s:
        heading = el.text.replace("\\n", "").lstrip().rstrip()
        # print("--heading--", heading)
        newSibling = el.find_next_sibling("ul")
        children = newSibling.findChildren("a")
        children_arr = []
        for child in children:
            child_str = child.text.replace("\\n", "").lstrip().rstrip()
            child_str_length = len(child_str)
            child_str = child_str[3:child_str_length]
            children_arr.append(child_str)
            # print(heading +", "+child_str)
        # print(new_str)
        genre_dict[heading]=children_arr


    genre_text_file = open("genre.json", "w+")
    genre_json = json.dumps(genre_dict)
    genre_text_file.write(genre_json)
    genre_text_file.close()
    # print(genreDict)

app()