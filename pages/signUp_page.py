from pages.base_page import BasePage
from locators.locators_signup_page import SignUp_Locators

class SignupPage(BasePage):
    def enter_name(self,name):
        self.input_text(*SignUp_Locators.Name_input,name)

    def enter_email(self,email):
        self.input_text(*SignUp_Locators.Email_Address_input,email)

    def click_signup(self):
        self.click_element(*SignUp_Locators.Signup_button)

    def get_new_user_signup_text(self):
        return self.get_element_text(*SignUp_Locators.New_user_signup_text)
