import time
import urllib
import requests
import splinter
import random

def SuggestedScrape():
    username = 
    password = 

    #username = 
    #password = 

    #Browser stuff
    """ profile = {
        'network.proxy.http': '140.227.237.154',
        'network.proxy.http_port': '1000',
        'network.proxy.ssl': '140.227.237.154',
        'network.proxy.ssl_port': '1000',
        'network.proxy.type': 1
    } """

    executable_path = {'executable_path': r'C:\Users\sfbow\Desktop\chromedriver'}
    browser = splinter.Browser('chrome', **executable_path, headless = False,)

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
    browser.visit('https://www.instagram.com/explore/people/suggested/')

    Follows = 1
    while True:
        try:
            browser.find_by_xpath('/html/body/div[1]/section/main/div/div[2]/div/div/div[{}]/div[3]/button'.format(Follows)).click()
            Follows += 1
            print(Follows - 1)
            time.sleep(random.randint(1,5))
        except:
            break
