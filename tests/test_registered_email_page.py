from pages.registered_email_page import RegisterdPage
from data.registered_email import Registered_email
from config.log_config import LoggerConfig
from pages.base_page import BasePage
from pages.home_page import HomePage
from config.url_config import urlConfig
from config.screenshot_file_config import screenshotFileConfig
def test_Registered_email(setup):
    registerd_log = LoggerConfig('test_Registered_email.log')
    #base_page = BasePage(setup)
    home_page = HomePage(setup)

    registerd_page = RegisterdPage(setup)
    registerd_log.logger.info("Start Registerd Email signup execution")
    registerd_page.navigate_to_url(urlConfig.base_url)

    assert registerd_page.get_page_title(),"Automation Exercise"
    registerd_page.capture_screenshot(screenshotFileConfig.screenshot_file_location_common + "\\screenshot_homepage.png")
    registerd_log.logger.info("Home page displayed")

    home_page.click_Signup_Login()

    registerd_log.logger.info("SignUp button from home page press successfully")
    assert registerd_page.get_new_user_signup_text(),"New User Signup!"
    registerd_page.capture_screenshot(screenshotFileConfig.screenshot_file_location_registerdemail + "\\screenshot_SignupPage.png")
    registerd_log.logger.info("New User Signup section displayed")

    registerd_page.enter_name(Registered_email.name)
    registerd_log.logger.info("Enter name successfully")
    registerd_page.enter_email(Registered_email.email)
    registerd_log.logger.info("Enter email successfully")
    registerd_page.click_signup()
    registerd_log.logger.info("press signup button successfully")

    assert registerd_page.get_email_already_exist_message(), "Email Address already exist!"
    registerd_page.capture_screenshot(screenshotFileConfig.screenshot_file_location_registerdemail + "\\screenshot_email_exist.png")
    registerd_log.logger.info("Email alredy exist message displayed")

    registerd_log.close_logger()