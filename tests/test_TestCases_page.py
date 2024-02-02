import time
from pages.testCases_page import TestCasePage
from config.log_config import LoggerConfig
from pages.base_page import BasePage
from pages.home_page import HomePage
from config.url_config import urlConfig
from config.screenshot_file_config import screenshotFileConfig

def test_Contact_Us(setup):
    Test_log = LoggerConfig('test_cases_page.log')
    # base_page = BasePage(setup)
    home_page = HomePage(setup)

    test_page = TestCasePage(setup)
    Test_log.logger.info("Start Test Cases Page execution")
    test_page.navigate_to_url(urlConfig.base_url)

    assert test_page.get_page_title(), "Automation Exercise"
    test_page.capture_screenshot(screenshotFileConfig.screenshot_file_location_common + "\\screenshot_homepage.png")
    Test_log.logger.info("Home page displayed")

    home_page.click_Test_Cases()
    Test_log.logger.info("Test Cases button from home page press successfully")

    assert test_page.get_Test_Cases_Text(), "TEST CASES"
    test_page.capture_screenshot(
        screenshotFileConfig.screenshot_file_location_testCases + "\\screenshot_testCase.png")
    Test_log.logger.info("Test Cases Section displayed")

    Test_log.close_logger()


