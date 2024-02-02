from pages.base_page import BasePage
from locators.locators_productDetails_page import ProductDetails_Locators

class ProductDetailsPage(BasePage):
    # Check Element visibility in specific section
    def productlist_visible(self):
        return self.is_element_displayed(*ProductDetails_Locators.product_list)

    def productdetails_visible(self):
        return self.is_element_displayed(*ProductDetails_Locators.product_details)

    # Click View Product
    def click_view_product(self):
        self.click_element(*ProductDetails_Locators.view_product_button)

    def get_all_products_text(self):
        return self.get_element_text(*ProductDetails_Locators.all_products_text)