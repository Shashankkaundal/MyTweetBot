import time

import pytest
from src.pages.LoginPage import *
@pytest.mark.usefixtures("init_driver")
class TestLoginNegative:
    #@pytest.mark.tcid12
    def test_login_none_exisiting_user(self):
        myaccount=LoginPage(self.driver)
        myaccount.go_to_my_account()
        myaccount.input_login_username('shashankkaundal@gmail.com')
        myaccount.click_next_button()
        myaccount.input_phone_number('Shashankkaundal')
        myaccount.click_2step_next_button()
        myaccount.input_login_password('Bethebest@31')
        myaccount.click_login_button()
        time.sleep(25)
        #expected_error="The username Hello@123@gmail.com is not registered on this site. If you are unsure of your username, try your email address instead."
        #myaccount.wait_until_error_is_displayed(expected_error)
        #assert expected_error==abc,f"something is wrong"
