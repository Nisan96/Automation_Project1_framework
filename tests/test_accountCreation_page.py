import time
from data.account_create import Account_Create
from data.sign_up import SignUp
from config.screenshot_file_config import screenshotFileConfig
from config.log_config import LoggerConfig
from pages.account_Creation_page import AccountCreation
from pages.home_page import HomePage
from pages.signUp_page import SignupPage
from config.url_config import urlConfig

def test_accountCreation(setup):
    account = AccountCreation(setup)
    account_log = LoggerConfig('test_account_creation.log')

    home_page = HomePage(setup)
    signup_page = SignupPage(setup)

    account.navigate_to_url(urlConfig.base_url)
    home_page.click_Signup_Login()

    signup_page.enter_name(SignUp.name)
    signup_page.enter_email(SignUp.Email)
    signup_page.click_signup()

    assert account.get_enter_account_information_text(),"ENTER ACCOUNT INFORMATION"
    account.capture_screenshot(screenshotFileConfig.screenshot_file_location_accountCreation + "\\account_creation.png")
    account_log.logger.info("enter account info is visible")

    account.enter_password(Account_Create.password)
    account.enter_first_name(Account_Create.firstname)
    account.enter_last_name(Account_Create.lastname)
    account.enter_company(Account_Create.company)
    account.enter_address1(Account_Create.address1)
    account.enter_address2(Account_Create.address2)
    account.enter_state(Account_Create.state)
    account.enter_city(Account_Create.city)
    account.enter_zipcode(Account_Create.zipcode)
    account.enter_mobile(Account_Create.mobile_number)
    account.select_day(Account_Create.day)

    account.select_month(Account_Create.month)
    account.select_year(Account_Create.year)
    account.select_country(Account_Create.country)
    account.select_title()
    account_log.logger.info("Sucessfully Fill details: Title, Name, Email, Password, Date of birth,country,state etc")
    account.click_news_letter()
    account_log.logger.info("Select checkbox 'Sign up for our newsletter' Successfully")
    account.click_special_offer()
    account_log.logger.info("Select checkbox 'Receive special offers from our partners!'Successfully")
    account.click_create_account_button()
    account_log.logger.info("click create account button successfully")

    assert account.get_account_created_text(),"ACCOUNT CREATED!"
    account.capture_screenshot(screenshotFileConfig.screenshot_file_location_accountCreation + "\\account_creation_message.png")
    account_log.logger.info("Account Created Message Shown Successfully")

    option = account.get_day_dropdown_all_options()
    print(option)
    account_log.logger.info(option)

    account_log.close_logger()