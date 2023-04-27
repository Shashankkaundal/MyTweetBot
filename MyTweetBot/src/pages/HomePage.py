import time

from SeleniumExtended import SeleniumExtended
from src.pages.locators.Homepagetweetloc import HomePageTweetLocators
from src.helpers.config_helpers import get_base_url
from selenium.webdriver import *

class HomePage(HomePageTweetLocators):
    #accountlink = '/my-account/'


    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)
    def input_tweet(self,tweet):
        #time.sleep(20)
        self.sl.wait_and_click_btn(self.tweetwindow)
        self.sl.wait_and_input_text(self.tweetwindow,tweet)
        #self.driver.
    def click_tweet_button(self):
        self.sl.wait_and_click_btn(self.tweetbutton)

    def capture_screenshot(self):
        self.sl.save_screenshot()
