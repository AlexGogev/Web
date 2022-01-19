import requests
from bs4 import BeautifulSoup
import html

response = requests.get(url="https://www.empireonline.com/movies/features/best-movies-2/").text
soup = BeautifulSoup(response, "html.parser")

get_tags = soup.find_all(class_="jsx-4245974604")


with open("movies.txt", "w", encoding='utf8') as text:
    for i in get_tags:
        text.write(f'{i.getText()}\n')


