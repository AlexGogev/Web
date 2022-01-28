from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import os

USER_NAME = ""
PASSWORD = os.environ["password"]
user = input("1 For Anna \n2 For Alex\n---> ")
if user == "1":
    USER_NAME = os.environ["AnnaEmail"]
elif user == "2":
    USER_NAME = os.environ["AlexEmail"]


driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://www.bing.com")
time.sleep(2)
accept = driver.find_element_by_xpath('//*[@id="bnp_btn_accept"]/a')
accept.click()

sign_in = driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/header/div[2]/div/a[1]/span[1]")
sign_in.click()

time.sleep(1.5)
user_field = driver.find_element_by_xpath('//*[@id="i0116"]')
user_field.click()
user_field.send_keys(USER_NAME)

time.sleep(1.5)
next = driver.find_element_by_xpath('/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div[3]/div/div/div/div[4]/div/div/div/div/input')
next.click()

time.sleep(1.5)
password = driver.find_element_by_xpath('/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[3]/div/div[2]/div/div[3]/div/div[2]/input')
password.send_keys(PASSWORD)

time.sleep(2)
login = driver.find_element_by_xpath('/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[3]/div/div[2]/div/div[4]/div[2]/div/div/div/div/input')
login.click()

time.sleep(2)
yes = driver.find_element_by_xpath('/html/body/div/form/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[3]/div/div[2]/div/div[3]/div[2]/div/div/div[2]/input')
yes.click()

time.sleep(1)
main_search = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/form/input[1]')
main_search.send_keys("number ")
main_search.send_keys(Keys.ENTER)

time.sleep(1.3)
for i in range(30):
    search_loop = driver.find_element_by_class_name("b_searchbox")
    search_loop.click()
    time.sleep(0.3)
    search_loop.send_keys(Keys.BACKSPACE)
    search_loop.send_keys(i)
    search_loop.send_keys(Keys.ENTER)
    time.sleep(1)