import requests
from bs4 import BeautifulSoup
response = requests.get(url="https://vicove.com/novi-vicove/2").text


vic = BeautifulSoup(response, "html.parser")

haha = vic.find_all(class_="joke_text")
vic_list = []
for i in haha:
    vic_list.append(i.getText())

print(vic_list)