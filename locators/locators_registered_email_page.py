from selenium.webdriver.common.by import By

class Registerd_Locators:
    ##  define locators
    Name_input = (By.CSS_SELECTOR, "[type='text']")
    Email_Address_input = (By.CSS_SELECTOR, ".signup-form > form[method='post'] > input[name='email']")
    Signup_button = (By.CSS_SELECTOR, ".signup-form > form[method='post'] > .btn.btn-default")

    Email_exist_message = (By.CSS_SELECTOR, "[action] p")

    New_user_signup_message = (By.CSS_SELECTOR, ".signup-form h2")