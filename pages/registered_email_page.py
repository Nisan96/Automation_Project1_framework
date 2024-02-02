from pages.base_page import BasePage
from locators.locators_registered_email_page import Registerd_Locators

class RegisterdPage(BasePage):
    def enter_name(self,name):
        self.input_text(*Registerd_Locators.Name_input,name)

    def enter_email(self,email):
        self.input_text(*Registerd_Locators.Email_Address_input,email)

    def click_signup(self):
        self.click_element(*Registerd_Locators.Signup_button)

    def get_new_user_signup_text(self):
        return self.get_element_text(*Registerd_Locators.New_user_signup_message)

    def get_email_already_exist_message(self):
        return self.get_element_text(*Registerd_Locators.Email_exist_message)
