from pages.base_page import BasePage
from locators.locators_home_page import HomePage_Locators

class HomePage(BasePage):
    def click_Signup_Login(self):
        self.click_element(*HomePage_Locators.signup_login_button)

    def click_Contact_Us(self):
        self.click_element(*HomePage_Locators.Contact_Us_button)

    def click_Test_Cases(self):
        self.click_element(*HomePage_Locators.Test_Cases_button)

    def click_Products(self):
        self.click_element(*HomePage_Locators.Products_button)