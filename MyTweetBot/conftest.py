import pytest
from selenium import webdriver
import os

@pytest.fixture(scope="class")
def init_driver(request):
    supported_browsers=['chrome','ch','headlesschrome','firefox','ff']
    browser=os.environ.get('BROWSER',None)
    if not browser:
        raise Exception("The env variable browser must be set")
    browser=browser.lower()
    if browser not in supported_browsers:
      raise Exception(f"Provided browser '{browser}' is not one of the supported"
                      f"Supported are '{supported_browsers}'")
    if browser in ('chrome','ch'):
        driver=webdriver.Chrome()
    elif browser in ('firefox','ff'):
        driver=webdriver.Firefox()
    request.cls.driver=driver
    yield

# export BROWSER=chrome use this for mac