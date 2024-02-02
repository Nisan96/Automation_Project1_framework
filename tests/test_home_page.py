from config.log_config import LoggerConfig
from pages.base_page import BasePage
from config.url_config import urlConfig
from config.screenshot_file_config import screenshotFileConfig
from pages.home_page import HomePage

def test_homepage(setup):
    homepage_log = LoggerConfig('test_homepage.log')

    home_page = HomePage(setup)
    homepage_log.logger.info("Start Homepage execution")
    home_page.navigate_to_url(urlConfig.base_url)
    home_page.click_Signup_Login()

    homepage_log.close_logger()