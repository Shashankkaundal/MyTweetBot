from selenium.webdriver.common.by import By

class MyLogInLocators():
    username=(By.XPATH,"//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")
    nextbutton=(By.XPATH,"//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]")
    password=(By.XPATH,"//div[@class='css-1dbjc4n r-mk0yit r-1f1sjgu']/label/div/div[@class='css-1dbjc4n r-18u37iz r-16y2uox r-1wbh5a2 r-1wzrnnt r-1udh08x r-xd6kpl r-1pn2ns4 r-ttdzmv']/div[@dir='ltr']/input[@name='password']")
    loginbutton=(By.XPATH,"//div[@role='button']/div[@dir='ltr']/span/span[contains(text(),'Log in')]")
    step_2_verification=(By.XPATH,"//div/div[@dir='ltr']/input[@name='text']")
    step_2_next_button=(By.XPATH,"//div[@class='css-1dbjc4n r-pw2am6']/div/div[@dir='ltr']/span/span[contains(text(),'Next')]")