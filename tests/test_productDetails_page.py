import time
from pages.product_details_page import ProductDetailsPage
from config.log_config import LoggerConfig
from pages.base_page import BasePage
from pages.home_page import HomePage
from config.url_config import urlConfig
from config.screenshot_file_config import screenshotFileConfig

def test_Product_details(setup):
    details_log = LoggerConfig('test_product_details.log')
    #base_page = BasePage(setup)
    home_page = HomePage(setup)

    details_page = ProductDetailsPage(setup)
    details_log.logger.info("Start Product Details Page execution")
    details_page.navigate_to_url(urlConfig.base_url)

    assert details_page.get_page_title(),"Automation Exercise"
    details_page.capture_screenshot(screenshotFileConfig.screenshot_file_location_common + "\\screenshot_homepage.png")
    details_log.logger.info("Home page displayed")

    home_page.click_Products()
    details_log.logger.info("Products button from home page press successfully")
    assert details_page.get_all_products_text(),"ALL PRODUCTS"
    details_page.capture_screenshot(screenshotFileConfig.screenshot_file_location_productDetails + "\\screenshot_allProducts.png")
    details_log.logger.info("All Products section displayed")

    if details_page.productlist_visible() == True:
        details_log.logger.info("Product List is visible")
    else:
        details_log.logger.info("Product List is not visible")

    details_page.click_view_product()
    details_log.logger.info("click view product successfully")
    assert details_page.get_page_title(), "Automation Exercise - Product Details"
    details_log.logger.info("landed on product details page")
    if details_page.productdetails_visible() == True:
        details_log.logger.info("Product Details (product name, category, price, availability, condition, brand) is visible")
        details_page.capture_screenshot(
            screenshotFileConfig.screenshot_file_location_productDetails + "\\screenshot_productDetails.png")
    else:
        details_log.logger.info("Product Details is not visible")


    details_log.close_logger()