import time
from pages.contact_us_page import ContactPage
from data.contact_us import ContactUs
from config.log_config import LoggerConfig
from pages.base_page import BasePage
from pages.home_page import HomePage
from config.url_config import urlConfig
from config.screenshot_file_config import screenshotFileConfig

def test_Contact_Us(setup):
    contact_log = LoggerConfig('test_contact_us.log')
    #base_page = BasePage(setup)
    home_page = HomePage(setup)

    contact_page = ContactPage(setup)
    contact_log.logger.info("Start Contact Us Page execution")
    contact_page.navigate_to_url(urlConfig.base_url)

    assert contact_page.get_page_title(),"Automation Exercise"
    contact_page.capture_screenshot(screenshotFileConfig.screenshot_file_location_common + "\\screenshot_homepage.png")
    contact_log.logger.info("Home page displayed")

    home_page.click_Contact_Us()
    contact_log.logger.info("Contact Us button from home page press successfully")
    assert contact_page.get_in_touch_message(),"GET IN TOUCH"
    contact_page.capture_screenshot(screenshotFileConfig.screenshot_file_location_contactus + "\\screenshot_ContactUs.png")
    contact_log.logger.info("Get In Touch section displayed")

    contact_page.enter_name(ContactUs.name)
    contact_log.logger.info("Type name successfully")
    contact_page.enter_email(ContactUs.email)
    contact_log.logger.info("Type email successfully")
    contact_page.enter_subject(ContactUs.subject)
    contact_log.logger.info("Type subject successfully")
    contact_page.enter_message(ContactUs.message)
    contact_log.logger.info("Type message successfully")
    contact_page.upload_choose_file(ContactUs.file_path)
    contact_log.logger.info("File Choosen successfully")
    time.sleep(2)
    contact_page.click_submit()
    contact_log.logger.info("Submit button clicked successfully")

    contact_page.press_OK_alert()

    assert contact_page.submit_status(), "Success! Your details have been submitted successfully."
    contact_page.capture_screenshot(
        screenshotFileConfig.screenshot_file_location_contactus + "\\screenshot_ContactUs_submit.png")

    contact_page.back_home()
    contact_page.capture_screenshot(
        screenshotFileConfig.screenshot_file_location_contactus + "\\screenshot_back_home.png")

    contact_log.logger.info("Back Home successfully")


    contact_log.close_logger()