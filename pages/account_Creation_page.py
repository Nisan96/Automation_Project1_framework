from pages.base_page import BasePage
from locators.locators_accountCreation_page import accountCreation_locators
class AccountCreation(BasePage):
    def get_enter_account_information_text(self):
        return self.get_element_text(*accountCreation_locators.ENTER_ACCOUNT_INFORMATION)

    def select_title(self):
        self.click_element(*accountCreation_locators.TITLE_RADIO)

    def enter_password(self, password):
        self.input_text(*accountCreation_locators.PASSWORD, password)

    def select_day(self, value):
        self.select_dropdown_option_by_value(*accountCreation_locators.DAY, value)

    def select_month(self, value):
        self.select_dropdown_option_by_value(*accountCreation_locators.MONTH, value)

    def select_year(self, value):
        self.select_dropdown_option_by_value(*accountCreation_locators.YEAR, value)

    def click_news_letter(self):
        self.click_element(*accountCreation_locators.NEWS_LETTER)

    def click_special_offer(self):
        self.click_element(*accountCreation_locators.SPECIAL_OFFER)

    def enter_first_name(self, firstname):
        self.input_text(*accountCreation_locators.FIRST_NAME, firstname)

    def enter_last_name(self, lastname):
        self.input_text(*accountCreation_locators.LAST_NAME, lastname)

    def enter_company(self, company):
        self.input_text(*accountCreation_locators.COMPANY, company)

    def enter_address1(self, address1):
        self.input_text(*accountCreation_locators.ADDRESS1, address1)

    def enter_address2(self, address2):
        self.input_text(*accountCreation_locators.ADDRESS2, address2)

    def select_country(self, value):
        self.select_dropdown_option_by_value(*accountCreation_locators.COUNTRY, value)

    def enter_state(self, state):
        self.input_text(*accountCreation_locators.STATE, state)

    def enter_city(self, city):
        self.input_text(*accountCreation_locators.CITY, city)

    def enter_zipcode(self, zipcode):
        self.input_text(*accountCreation_locators.ZIPCODE, zipcode)

    def enter_mobile(self, mobile):
        self.input_text(*accountCreation_locators.MOBILE, mobile)

    def click_create_account_button(self):
        self.click_element(*accountCreation_locators.CREATE_ACCOUNT_BUTTON)

    def get_day_dropdown_all_options(self):
        return self.get_dropdown_options(*accountCreation_locators.DAY)

    def get_account_created_text(self):
        return self.get_element_text(*accountCreation_locators.account_created)
