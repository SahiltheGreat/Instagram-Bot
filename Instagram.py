from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import getpass
import time


class InstagramBot:

    def __init__(self):
        print("Enter Email-ID:")
        self.username = input()
        print("Enter your Instagram password")
        self.password = getpass.getpass()

        #For Firefox
        self.driver = webdriver.Firefox()
        
        #For Chrome
        # self.driver = webdriver.Chrome()

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        driver.maximize_window()
        time.sleep(2)
        
        # If logging in using email
        # login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        # login_button.click()
        
        # If logging in using Facebook
        login_button = driver.find_element_by_xpath('//button[@class="_0mzm- sqdOP  L3NKy       "]')
        login_button.click()
        time.sleep(2)
        username_field = driver.find_element_by_xpath('//input[@name="email"]')
        username_field.clear()
        username_field.send_keys(self.username)
        password_field = driver.find_element_by_xpath('//input[@name="pass"]')
        password_field.clear()
        password_field.send_keys(self.password)
        time.sleep(2)
        password_field.send_keys(Keys.RETURN)
        time.sleep(3)

    def like_photo(self,hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(2)
        for i in range(1,3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
        
        hrefs = driver.find_element_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        pic_hrefs = [href for href in pic_hrefs if hashtag in href]
        print(hashtag + 'photos: '+  str(len(pic_hrefs)))

    
# print("Enter your Insta account password:")
autobot = InstagramBot()
autobot.login()
autobot.like_photo("starwars")