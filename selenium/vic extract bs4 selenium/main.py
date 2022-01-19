from selenium import webdriver
from bs4 import BeautifulSoup
import random
page_number = random.randint(1,18)
path_to_driver = "C:/Users/Alex/Desktop/Web/selenium/chromedriver.exe"
driver = webdriver.Chrome(executable_path=path_to_driver)
    #Edge("msedgedriver.exe")
    #Chrome(executable_path=path_to_driver)



driver.get(f"https://www.vicove.bg/page/{page_number}")

#class("post-discription"
with open("page_source.html", "w") as html:
    html.write(driver.page_source)
driver.quit



with open("page_source.html", "r") as extracted_from_selenium:
    contents = extracted_from_selenium.read()

soup = BeautifulSoup(contents, "html.parser")
vic = soup.find_all(name="p")
#class_="post-discription"
for i in vic:
    print(i.getText())