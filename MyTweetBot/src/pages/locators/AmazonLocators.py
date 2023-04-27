from selenium.webdriver.common.by import By

class AmazonLocators():
    searchfield=(By.CSS_SELECTOR,"input[name='field-keywords']")
    searchbutton=(By.CSS_SELECTOR,"input[id='nav-search-submit-button']")
    searchlist=(By.XPATH,"//h2/a/span[contains(text(),'Sony PS5 Digital Standalone')]")
    buynow=(By.XPATH,"//span/span[contains(text(),' Buy Now ')]")

