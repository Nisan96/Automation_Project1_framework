from pages.signUp_page import SignupPage
from data.sign_up import SignUp
from config.log_config import LoggerConfig
from pages.base_page import BasePage
from pages.home_page import HomePage
from config.url_config import urlConfig
from config.screenshot_file_config import screenshotFileConfig
def test_signup(setup):
    signup_log = LoggerConfig('test_signup.log')
    #base_page = BasePage(setup)
    home_page = HomePage(setup)

    signup_page = SignupPage(setup)
    signup_log.logger.info("Start SignUp execution")
    signup_page.navigate_to_url(urlConfig.base_url)

    assert signup_page.get_page_title(),"Automation Exercise"
    signup_page.capture_screenshot(screenshotFileConfig.screenshot_file_location_common + "\\screenshot_homepage.png")
    signup_log.logger.info("Home page displayed")

    home_page.click_Signup_Login()
    signup_log.logger.info("SignUp button from home page press successfully")
    assert signup_page.get_new_user_signup_text(),"New User Signup!"
    signup_page.capture_screenshot(screenshotFileConfig.screenshot_file_location_signup + "\\screenshot_SignupPage.png")
    signup_log.logger.info("New User Signup section displayed")

    signup_page.enter_name(SignUp.name)
    signup_log.logger.info("Enter name successfully")
    signup_page.enter_email(SignUp.email)
    signup_log.logger.info("Enter email successfully")
    signup_page.click_signup()
    signup_log.logger.info("press signup button successfully")

    if signup_page.get_page_title() == "Automation Exercise - Signup":
        signup_page.capture_screenshot(
            screenshotFileConfig.screenshot_file_location_signup + "\\screenshot_Create_account.png")
        signup_log.logger.info("signup successfully")
    else:
        signup_log.logger.info("can't signup....raise some problem")

    signup_log.close_logger()



