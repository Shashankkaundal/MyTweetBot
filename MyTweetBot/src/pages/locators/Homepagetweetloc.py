from selenium.webdriver.common.by import By
from selenium import webdriver

class HomePageTweetLocators():

    tweetwindow=(By.XPATH,"//div[@role='textbox']")
    tweetbutton=(By.XPATH,"//div[@role='button']/div[@dir='ltr']/span/span[contains(text(),'Tweet')]")