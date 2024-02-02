import time
from pages.search_product_page import SearchProductPage
from data.search_product import product_search
from config.log_config import LoggerConfig
from pages.base_page import BasePage
from pages.home_page import HomePage
from config.url_config import urlConfig
from config.screenshot_file_config import screenshotFileConfig

def test_Search_Product(setup):

    search_log = LoggerConfig('test_searchProduct.log')
    #base_page = BasePage(setup)
    home_page = HomePage(setup)

    product_page = SearchProductPage(setup)
    search_log.logger.info("Start Search Product Page execution")
    product_page.navigate_to_url(urlConfig.base_url)

    assert product_page.get_page_title(),"Automation Exercise"
    product_page.capture_screenshot(screenshotFileConfig.screenshot_file_location_common + "\\screenshot_homepage.png")
    search_log.logger.info("Home page displayed")

    home_page.click_Products()
    search_log.logger.info("Products button from home page press successfully")

    if product_page.get_all_products_text() == True:
        product_page.capture_screenshot(
            screenshotFileConfig.screenshot_file_location_searchProduct + "\\screenshot_allProducts.png")
        search_log.logger.info("Navigated to ALL PRODUCTS page Successfully")

    else:
        search_log.logger.info("ALL PRODUCTS page is not displayed")

    product_page.search_product(product_search.product_name)
    search_log.logger.info("Input product name in searchBox successfully")

    product_page.click_search_button()
    search_log.logger.info("click search button successfully")

    if product_page.Searched_Product_Text() == "SEARCHED PRODUCTS":
        search_log.logger.info("---Searched Products Section is visible---")
        product_page.capture_screenshot(screenshotFileConfig.screenshot_file_location_searchProduct + "\\screenshot_searchProduct.png")
        search_log.logger.info("---The Product related to search are visible---")
    else:
        search_log.logger.info("---Searched Products Section is not visible---")

    '''if product_page.first_Product_Text() == "Men Tshirt":
        search_log.logger.info("---The Product related to search are visible---")
        product_page.capture_screenshot(
            screenshotFileConfig.screenshot_file_location_searchProduct + "\\screenshot_searchProduct.png")
    else:
        search_log.logger.info("---The Product related to search are not visible---")'''


    search_log.close_logger()