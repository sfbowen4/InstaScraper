import time
import urllib
import requests
import splinter
import random
import SuggestedScraper

username = 'bigchungy420693.0'
password = 'ClearlyInventory2020!'

#username = 'cordlove.organizer'
#password = 'ClearlyInventory2020!'

hashtag = ['Laptop','Creativity','styleinspiration','styleoftheday','stylegram','styled','styleformen','styleguide','styleaddict','stylebloggers','styleicon','stylemen','stylelife','technology','techno','techie','technique','techy','technics','technical','technopreneur','techlife','techstartup','technolove','technician','techies','technologies','techgeek','technolovers']
print(len(hashtag))
HashTagCounter = 0
hashtagpage = 'https://www.instagram.com/explore/tags/{}'.format(hashtag)

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

ErrorCounter = 0
SessionFollows = 0
while True:
    Follows = 0
    try:
        hashtagpage = 'https://www.instagram.com/explore/tags/{}'.format(hashtag[HashTagCounter])
    except:
        print('Done!')
    browser.visit(hashtagpage)
    time.sleep(1)
    FirstThumbnail = browser.find_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div')
    FirstThumbnail.click()
    time.sleep(1)
    try:
        while Follows <= 14:
            FollowToggle = browser.find_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button')
            if browser.is_text_present('Following') == True:
                browser.find_link_by_text('Next').click()
            else:
                time.sleep(random.randint(20,60))  
                FollowToggle.click()
                try:
                    browser.find_link_by_text('Next').click()
                    Follows += 1
                    SessionFollows += 1
                except:
                    pass
                print(SessionFollows)
    except:
        time.sleep(30)
        print('Ran into connection or limit error.')
        ErrorCounter += 1
        if ErrorCounter >= 1:
            #SWITCH IP
            print("Switch IP!")
            time.sleep(120)
        elif ErrorCounter >= 2:
            print("2 errors in a row. Waiting 10 minutes.")
            SuggestedScraper.SuggestedScrape()
            time.sleep(600)
            ErrorCounter = 0

    HashTagCounter += 1
