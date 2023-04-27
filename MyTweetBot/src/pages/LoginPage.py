from SeleniumExtended import SeleniumExtended
from src.pages.locators.LoginPageLocators import MyLogInLocators
from src.helpers.config_helpers import get_base_url

class LoginPage(MyLogInLocators):
    #accountlink = '/my-account/'

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)
    def go_to_my_account(self):
        base_url = get_base_url()
        #my_account_url = base_url + self.accountlink
        self.driver.get(base_url)
        #logger.info(f"gooing to login")

    def input_login_username(self,username):
        self.sl.wait_and_input_text(self.username,username)

    def click_next_button(self):
        self.sl.wait_and_click_btn(self.nextbutton)

    # def click_on_phno_field(self):
    #     self.sl.wait_and_click_btn(self.step_2_verification)

    def input_phone_number(self,phone):
        #self.sl.wait_and_click_btn(self.step_2_verification)
        self.sl.wait_and_input_text(self.step_2_verification,phone)

    def click_2step_next_button(self):
        self.sl.wait_and_click_btn(self.step_2_next_button)

    def input_login_password(self,password):
        self.sl.wait_and_input_text(self.password,password)

    def click_login_button(self):
        self.sl.wait_and_click_btn(self.loginbutton)
        #logger.debug(f"clicking the button")

