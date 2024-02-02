from pages.base_page import BasePage
from locators.locators_search_product_page import SearchProduct_Locators

class SearchProductPage(BasePage):
    def get_all_products_text(self):
        return self.is_element_displayed(*SearchProduct_Locators.all_products_text)

    def search_product(self,product):
        self.input_text(*SearchProduct_Locators.search_input, product)

    def click_search_button(self):
        self.click_element(*SearchProduct_Locators.search_button)

    def Searched_Product_Text(self):
        return self.get_element_text(*SearchProduct_Locators.searched_product_text)

    def first_Product_Text(self):
        return self.get_element_text(*SearchProduct_Locators.verify_product_text)