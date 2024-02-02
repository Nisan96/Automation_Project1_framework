from pages.base_page import BasePage
from locators.locators_testcases_page import TestCases_Locators

class TestCasePage(BasePage):
    def get_Test_Cases_Text(self):
        return self.get_element_text(*TestCases_Locators.Test_Cases_text)
