
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


# Website url
URL = "https://www.google.com/"
# Chromium Drivers
# Replace path of the chromium drivers with the directory in which you have your chromium drivers 
PATH = Service('C:\Program Files (x86)\chromedriver.exe')
# i am using google chrome that's why i have webdriver.chrome option 
# You can replace it with , edge options, firefox options etc.
OP = webdriver.ChromeOptions()
DRIVER = webdriver.Chrome(service=PATH, options=OP)

#  the search keyword 
search_keyword = "cricket"
# Navigate to the website using get method 
DRIVER.get(URL)




# find the search input field using find by element by method
search_field = DRIVER.find_element(By.NAME, "q")

# using send_keys method i am writing the string for search:
search_field.send_keys(search_keyword)
# Find the Google Search button
search_button = DRIVER.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]')
search_button.click()
assert search_keyword in DRIVER.title
# Hold on the page 
time.sleep(5)