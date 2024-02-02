from selenium.webdriver.common.by import By
class ContactUs_Locators:
    Get_in_touch_message = (By.CSS_SELECTOR, ".contact-form > .text-center.title")
    Name = (By.CSS_SELECTOR, "input[name='name']")
    Email = (By.CSS_SELECTOR, "input[name='email']")
    Subject = (By.CSS_SELECTOR, "input[name='subject']")
    Message = (By.CSS_SELECTOR, "#message")

    Submit_button = (By.CSS_SELECTOR, ".submit_form")

    Choose_file_button = (By.CSS_SELECTOR, "[name='upload_file']")

    Submit_status_message = (By.CSS_SELECTOR, ".status")

    Back_home_button = (By.CSS_SELECTOR, "span")
