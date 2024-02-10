from selenium.webdriver.common.by import By

class accountCreation_locators:
    ENTER_ACCOUNT_INFORMATION = (By.CSS_SELECTOR, ".login-form > .text-center.title > b")
    TITLE_RADIO = (By.CSS_SELECTOR, "[action] .radio-inline:nth-child(3) [type]")

    PASSWORD = (By.CSS_SELECTOR, "#password")
    DAY = (By.CSS_SELECTOR, "select#days")
    MONTH = (By.CSS_SELECTOR, "select#months")
    YEAR = (By.CSS_SELECTOR, "select#years")
    NEWS_LETTER = (By.CSS_SELECTOR, "#newsletter")
    SPECIAL_OFFER = (By.CSS_SELECTOR, "#optin")

    FIRST_NAME = (By.CSS_SELECTOR, "#first_name")
    LAST_NAME = (By.CSS_SELECTOR, "#last_name")
    COMPANY = (By.CSS_SELECTOR, "#company")
    ADDRESS1 = (By.CSS_SELECTOR, "input[name='address1']")
    ADDRESS2 = (By.CSS_SELECTOR, "input[name='address2']")
    COUNTRY = (By.CSS_SELECTOR, "select#country")
    STATE = (By.CSS_SELECTOR, "#state")
    CITY = (By.CSS_SELECTOR, "#city")
    ZIPCODE = (By.CSS_SELECTOR, "#zipcode")
    MOBILE = (By.CSS_SELECTOR, "#mobile_number")

    CREATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "section#form > .container form[method='post'] > .btn.btn-default")

    account_created = (By.CSS_SELECTOR, ".text-center.title > b")
