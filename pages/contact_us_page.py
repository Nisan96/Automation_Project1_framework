from pages.base_page import BasePage
from locators.locators_contact_us_page import ContactUs_Locators

class ContactPage(BasePage):
    def enter_name(self,name):
        self.input_text(*ContactUs_Locators.Name,name)

    def enter_email(self,email):
        self.input_text(*ContactUs_Locators.Email,email)

    def enter_subject(self,subject):
        self.input_text(*ContactUs_Locators.Subject,subject)

    def enter_message(self,message):
        self.input_text(*ContactUs_Locators.Message,message)

    def click_submit(self):
        self.click_element(*ContactUs_Locators.Submit_button)

    def upload_choose_file(self,file):
        return self.upload_file(*ContactUs_Locators.Choose_file_button, file)

    def get_in_touch_message(self):
        return self.get_element_text(*ContactUs_Locators.Get_in_touch_message)

    def press_OK_alert(self):
        self.accept_alert()

    def submit_status(self):
        return self.get_element_text(*ContactUs_Locators.Submit_status_message)

    def back_home(self):
        self.click_element(*ContactUs_Locators.Back_home_button)
