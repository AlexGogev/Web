from selenium import  webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://orteil.dashnet.org/cookieclicker/")

# Get cookie to click on.
cookie = driver.find_element_by_id("bigCookie")

for i in range(10000):
    cookie.click()