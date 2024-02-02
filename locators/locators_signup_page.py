from selenium.webdriver.common.by import By

class SignUp_Locators:
    ##  define locators
    Name_input = (By.CSS_SELECTOR, "[type='text']")
    Email_Address_input = (By.CSS_SELECTOR, "[action='\/signup'] [type='email']")
    Signup_button = (By.CSS_SELECTOR, "[action='\/signup'] .btn-default")
    New_user_signup_text = (By.CSS_SELECTOR, ".signup-form h2")


