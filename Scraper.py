import time
import urllib
import requests
import splinter

#username = 'bigchungy42069'
#password = 'ClearlyInventory2020!'

hashtag = 'house'
Follows = 0
Likes = 0
Comments = 0

hashtagpage = 'https://www.instagram.com/explore/tags/{}'.format(hashtag)
Follows = 201
Likes = 0
Comments = 0

#Browser stuff
executable_path = {'executable_path': r'C:\Users\sfbow\Desktop\chromedriver'}
browser = splinter.Browser('chrome', **executable_path, headless = False)

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

FirstThumbnail = browser.find_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div')
FirstThumbnail.click()
time.sleep(1)

while Follows < 100:
    if browser.is_text_present('Follow'):
        #FollowButton = browser.find_by_tag('button')[1]
        #FollowButton.click()
        print('FOLLOW')
        browser.find_link_by_text('Next').click()
    else:
        print('Already Followed')
        browser.find_link_by_text('Next').click()
    Follows += 1