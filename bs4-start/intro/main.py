from bs4 import BeautifulSoup
with open("website.html", "r") as html_data:
    contents = html_data.read()


#1st param is data, 2nd what type of data
# import lxml and pass "lxml" if html data is not valid
soup = BeautifulSoup(contents, "html.parser")  #soup becomes object to allow us tap in parts of the data
print(soup.title)
print(soup.title.name)
print(soup.title.string)

# print(soup.prettify())   #all html

print(soup.find_all(name="a")) #name = tag

'get text from a '
for i in soup.find_all(name="a"):
    print(i.getText()) #just text content
    print(i.get("href")) # just the links

"find specific"
"<h1 id='name'>Angela Yu</h1>"
heading = soup.find(name="h1", id="name") #id class_
print(heading)


"using (css or html nested) selector" #select_one - first match, select - all items
"<p><em>Founder of <strong><a href='https://www.appbrewery.co/'>The App Brewery</a></strong>.</em></p>"
company_url = soup.select_one(selector="p a") #"p a" is css/html selector can use also class_ or id
print(company_url)