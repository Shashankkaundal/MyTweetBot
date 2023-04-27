import time

import pytest
from src.pages.HomePage import *
@pytest.mark.usefixtures("init_driver")
class TestHomePageTweet:
    #@pytest.mark.tcid12
    def test_home_page_twwet(self):
        mytweet=HomePage(self.driver)
        mytweet.input_tweet("This is first automated tweet test")
        mytweet.click_tweet_button()
        time.sleep(25)