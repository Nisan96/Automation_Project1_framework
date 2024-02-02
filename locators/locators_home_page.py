from selenium.webdriver.common.by import By

class HomePage_Locators:
    ## define locators
    signup_login_button = (By.CSS_SELECTOR, "li:nth-of-type(4) > a")
    Contact_Us_button = (By.CSS_SELECTOR, "li:nth-of-type(8) > a")
    Test_Cases_button = (By.CSS_SELECTOR, "li:nth-of-type(5) > a")
    Products_button = (By.CSS_SELECTOR, ".nav.navbar-nav > li:nth-of-type(2) > a")