from bs4 import BeautifulSoup
import requests

SITE = "https://news.ycombinator.com/news"
response = requests.get(url=SITE).text

soup = BeautifulSoup(response, "html.parser")
articles_tag = soup.find_all(name="a", class_="titlelink")



article_text =[]
article_links = []
for i in articles_tag:
    article_text.append(i.getText())
    article_links.append(i.get("href"))
#article_link = article_tag.get("href")

article_upvote = [i.getText() for i in soup.find_all( class_="score")]


#print(article_upvote)
upvote_int = []

for i in article_upvote:

    x = i.split(" ")
    upvote_int.append((int(x[0])))

highest_vote = max(upvote_int)

highest_score = max(upvote_int)

target_index = upvote_int.index(highest_score)
print(article_text[int(target_index + 1)])
print(article_links[int(target_index + 1)])
print("votes ",highest_vote)

