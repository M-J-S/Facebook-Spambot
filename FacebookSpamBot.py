import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#variables needed to login to FB and then a friend/victim to choose by their FB ID to send messages to
userNameVariable = input("enter your Facebook email: ")
passwordVariable = input("enter your Facebook password: ")
friendVariable = input("enter your friend's facebook page ID: ")

#open facebook 
driver = webdriver.Chrome(executable_path="C:\Python34\Scripts\chromedriver")
driver.get("https://www.facebook.com/")

#use the credentials stored in above variables to log in
emailElem = driver.find_element_by_id('email')
emailElem.send_keys(userNameVariable)
passwordElem = driver.find_element_by_id('pass')
passwordElem.send_keys(passwordVariable)
passwordElem.submit()

#go to chat with chosen friend and enter this is a bot into message_body and hit enter
driver.get('https://facebook.com/messages/' + friendVariable)


#loop that will print 'this is a bot' every 10 seconds
while True:
    messageElem = driver.find_element_by_name('message_body')
    messageElem.send_keys('This is a bot')
    messageElem.send_keys(Keys.ENTER)
    time.sleep(10)
    
