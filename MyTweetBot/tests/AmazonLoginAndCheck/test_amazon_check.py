import time

import pytest
from src.pages.AmazonLoginAndCheck import *
@pytest.mark.usefixtures("init_driver")
class TestAmazonCheck:
    #@pytest.mark.tcid12
    def test_amazon_check(self):
        myamazon = AmazonLoginPageAndCheck(self.driver)
        myamazon.go_to_my_account()
        myamazon.input_search_field_text("Playstation 5")
        myamazon.click_search_button()
        myamazon.click_on_searchresults()
        val=myamazon.assert_on_buy_now()
        assert val=='Buy Now'
        time.sleep(25)