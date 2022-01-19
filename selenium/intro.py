from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://www.python.org/")

"""
driver.find_elements_by_css_selector if *
# use .css before actual css start
# use #id 
# space in css must.be.connected.by.dots

clicking on link -> click = driver.find_element_by_link_text() \n click.click()
search - line 53 
"""

data_text = driver.find_elements_by_css_selector(".medium-widget.event-widget.last")
#for i in data_text:
#   print(i.text)
time = []
info = []
link = []

data_time = driver.find_elements_by_css_selector(".medium-widget.event-widget.last .shrubbery .menu time")
for i in data_time:
    #print(i.text)
    time.append(i.text)

data_event = driver.find_elements_by_css_selector(".medium-widget.event-widget.last .shrubbery .menu a")
for i in data_event:
    #print(i.text)
    info.append(i.text)


data_link = driver.find_elements_by_css_selector(".medium-widget.event-widget.last .shrubbery .menu a")
for i in data_event:
    #print(i.get_attribute("href"))
    link.append(i.get_attribute("href"))
dict_info = {}
n=0
for i in time:
    dict_info[i] = [info[n],link[n]]
    n += 1

print(dict_info)



click = driver.find_element_by_link_text("Python Meeting Düsseldorf")
#click.click()


search = driver.find_element_by_name("q")
search.send_keys("zdr") #for clicking import line 2
search.send_keys(Keys.ENTER)


driver.find