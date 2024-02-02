from selenium.webdriver.common.by import By

class ProductDetails_Locators:
    product_list = (By.CSS_SELECTOR, "#accordian")
    view_product_button = (By.CSS_SELECTOR, "div:nth-of-type(2) > .product-image-wrapper > .choose > .nav.nav-justified.nav-pills  a")
    product_details = (By.CSS_SELECTOR, ".product-information")

    all_products_text = (By.CSS_SELECTOR, ".title")