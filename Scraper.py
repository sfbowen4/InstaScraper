import time
import urllib
import requests
from splinter import Browser


username = 'bigchungy42069'
password = 'ClearlyInventory2020!'
hashtag = 'trucks'
hashtagpage = 'https://www.instagram.com/explore/tags/{}'.format(hashtag)

#Browser stuff
executable_path = {'executable_path': r'/Users/stephen/Desktop/chromedriver'}
browser = Browser('chrome', **executable_path, headless = False)

#URL components
method = 'GET'
url = 'https://www.instagram.com/accounts/login/?source=auth_switcher'

browser.visit(url)

#define elements to pass through the form
browser.find_by_name("username").first.fill(username)
browser.find_by_name("password").first.fill(password)
browser.find_by_text("Log In").first.click()
time.sleep(2)

#save info
browser.find_by_text("Not Now").first.click()
time.sleep(2)
#turn on notifications
browser.find_by_text("Not Now").first.click()
time.sleep(2)
#go to hashtag page
browser.visit(hashtagpage)

links = []
tags = browser.links.find_by_partial_href('/p/')
for x in tags:
    links.append(x['href'])

for x in links:
    browser.visit(x)
    try:
        browser.find_by_text('Follow').first.click()
    except:
        print('Already Followed')
    time.sleep(5)
