import time

from selenium.common import TimeoutException, StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from PIL import Image
from selenium.webdriver.common.action_chains import ActionChains
class SeleniumExtended:
    def __init__(self,driver):
        self.driver=driver
        self.default_timeout=15

    def wait_and_input_text(self, locator, text, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def wait_and_click_btn(self,locator,timeout=None):
        try:
            timeout = timeout if timeout else self.default_timeout
            WebDriverWait(self.driver,timeout).until(EC.visibility_of_element_located(locator)).click()
        except StaleElementReferenceException:
            time.sleep(5)
            WebDriverWait(self.driver,timeout).until(EC.visibility_of_element_located(locator)).click()



    def wait_and_switch_amazon_window(self,locator,timeout=None):
        pass

    # def wait_until_element_contains_text(self,locator,text,timeout=None):
    #     timeout=timeout if timeout else self.default_timeout
    #     EC.text_to_be_present_in_element(locator,text)
    #
    # def wait_until_element_is_visible(self, locator, timeout=None):
    #     timeout = timeout if timeout else self.default_timeout
    #     EC.visibility_of_element_located(locator)
    #
    # def wait_and_get_elements(self, locator, timeout=None,err=None):
    #     timeout = timeout if timeout else self.default_timeout
    #     err=err if err else f"Unable to find elements located by '{locator}',"\
    #                         f"after timeout of {timeout}"
    #     try:
    #         elements=WebDriverWait(self.driver,timeout).until(
    #         EC.visibility_of_all_elements_located(locator))
    #     except TimeoutException:
    #         raise TimeoutException(err)
    #     return elements
    def wait_and_get_text(self,locator,timeout=None):
        window_before = self.driver.window_handles[0]
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        timeout = timeout if timeout else self.default_timeout
        elements = WebDriverWait(self.driver, timeout).until(
        EC.visibility_of_element_located(locator))
        element_text=elements.text
        #self.driver.switch_to.window(window_before)
        return element_text
    def wait_and_get_amazon_product_link(self,locator,timeout=None):
        window_before = self.driver.window_handles[0]
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        product_link = self.driver.current_url
        return product_link
    def save_screenshot(self):
        self.driver.save_screenshot("/Users/shashankkaundal/Downloads/MyTweetBot/Final_tweet.Png")



