from selenium.webdriver.common.by import By

class SearchProduct_Locators:
    all_products_text = (By.CSS_SELECTOR, ".title")

    search_input = (By.CSS_SELECTOR, "#search_product")
    search_button = (By.CSS_SELECTOR, ".fa-search")

    searched_product_text = (By.CSS_SELECTOR, ".title")

    verify_product_text = (By.CSS_SELECTOR, "div:nth-of-type(2) > .product-image-wrapper > .single-products > .product-overlay > .overlay-content > p")



