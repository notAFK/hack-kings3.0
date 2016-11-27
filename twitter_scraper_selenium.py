import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

base_url = 'https://twitter.com/search?q='
keyword = 'starbucks'
browser = webdriver.Chrome()
url = base_url + keyword

browser.get(url)
time.sleep(1)

body = browser.find_element_by_tag_name('body')

for _ in range(1000):
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)

tweets = browser.find_elements_by_class_name('tweet-text')

for tweet in tweets:
    print tweet.text.encode('utf-8')
