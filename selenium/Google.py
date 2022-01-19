from selenium import  webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

search_text = input("Enter what to search for? ")

option = webdriver.ChromeOptions()
option.add_argument("headless")

driver = webdriver.Chrome(executable_path="chromedriver.exe", options=option)
#driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://www.google.co.uk/")
agree = driver.find_element_by_xpath('//*[@id="L2AGLb"]/div')
agree.click()

time.sleep(1)

search = driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
search.send_keys(search_text)
search.send_keys(Keys.ENTER)

time.sleep(1)
ans = driver.find_element_by_xpath('//*[@id="Odp5De"]/div/div[1]/div/div[1]/div/div[2]/div/div/div[2]/div/span/span')
print(ans.text)
