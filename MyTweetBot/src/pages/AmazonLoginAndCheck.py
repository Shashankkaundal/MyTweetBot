from selenium.webdriver.support.wait import WebDriverWait

from SeleniumExtended import SeleniumExtended
from src.pages.locators.AmazonLocators import AmazonLocators
from src.helpers.config_helpers import get_amazon_url
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class AmazonLoginPageAndCheck(AmazonLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)
    def go_to_my_account(self):
        base_url = get_amazon_url()
        self.driver.get(base_url)

    def input_search_field_text(self,text):
        self.sl.wait_and_input_text(self.searchfield,text)

    def click_search_button(self):
        self.sl.wait_and_click_btn(self.searchbutton)

    def click_on_searchresults(self):
        self.sl.wait_and_click_btn(self.searchlist)

    def assert_on_buy_now(self):
        # switched to new window
        txt=self.sl.wait_and_get_text(self.buynow)
        return txt
    def amazon_product_link(self):
        link=self.sl.wait_and_get_amazon_product_link(self.buynow)
        return link

    def input_login_password(self,password):
        self.sl.wait_and_input_text(self.password,password)

    def click_login_button(self):
        self.sl.wait_and_click_btn(self.loginbutton)
        #logger.debug(f"clicking the button")

