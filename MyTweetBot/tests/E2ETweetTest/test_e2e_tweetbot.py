import time

import pytest
from src.pages.LoginPage import *
from src.pages.HomePage import *
from src.pages.AmazonLoginAndCheck import *
from src.helpers import *
@pytest.mark.usefixtures("init_driver")
class TestLoginNegative:
    #@pytest.mark.tcid12

    def test_login_none_exisiting_user(self):
        myaccount = LoginPage(self.driver)
        myamazon = AmazonLoginPageAndCheck(self.driver)
        mytweet = HomePage(self.driver)
        myamazon.go_to_my_account()
        myamazon.input_search_field_text('Playstation 5')
        myamazon.click_search_button()
        myamazon.click_on_searchresults()
        val = myamazon.assert_on_buy_now()
        linked = myamazon.amazon_product_link()
        if val == 'Buy Now':
            with open('/Users/shashankkaundal/Downloads/MyTweetBot/src/helpers/Credentials.txt', 'r') as file:
                text=file.readline()
            Username, Password, Email = text.strip().split()
            myaccount.go_to_my_account()
            myaccount.input_login_username(Email)
            myaccount.click_next_button()
            #below to be used in case of 2nd step twitter authentication
            #myaccount.input_phone_number(Username)
            #myaccount.click_2step_next_button()
            myaccount.input_login_password(Password)
            myaccount.click_login_button()
            mytweet.input_tweet(f"Play station 5 console is available on amazon india Click on following link {linked} to buy")
            mytweet.click_tweet_button()
            time.sleep(3)
            mytweet.capture_screenshot()

