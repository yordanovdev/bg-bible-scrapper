import requests
import json
from bs4 import BeautifulSoup
import re

with open('books.json') as f:
   books = json.load(f)

version = "BG1940"

data = {};

def is_null_or_whitespace(s):
    return s is None or s.isspace()

for book in books:
    book_name = book["usfm"]
    print(f"Starting {book['human']}")
    book_info = {}
    for chapter in book['chapters']:

        chapter_name = chapter["usfm"]
        url = f'https://www.bible.com/bible/23/{chapter_name}.{version}'

        print(f"Starting {chapter_name}")
        response = requests.get(url)

        chapter_info = {}

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            pattern = re.compile("^ChapterContent_verse__\w+")

            chapter_info_spans = soup.find_all('span', class_=pattern)

            for span in chapter_info_spans:
                id = span["data-usfm"]
                chapter_index = id.replace(f"{chapter_name}.", "")
                text = span.text
                if text.startswith(chapter_index):
                    text = text[len(chapter_index):]
                if is_null_or_whitespace(text):
                    continue
                chapter_info[chapter_index] = text
        book_info[chapter_name] = chapter_info
    data[book_name] = book_info

with open("data.json", "w") as a:
    json.dump(data, a, ensure_ascii=False, indent=2)
    a.close()
