from selenium.common import TimeoutException, NoSuchWindowException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from config.url_config import urlConfig

class BasePage:
    def __init__(self, control):
        self.control = control

    def wait_for_element(self,by,value,timeout=10):
        return WebDriverWait(self.control, timeout).until(ec.visibility_of_element_located((by, value)))

    def input_text(self, by, value, text):
        """
        Waits for the presence of an element, clears its content, and inputs the specified text.

        Parameters:
            by: The method used to locate the element (e.g., By. ID, By.NAME, By.XPATH, etc.).
            value: The value of the method (e.g., the ID, name, or XPath expression).
            text: The text to input into the element.

        Usage:
            base_page.input_text(By.ID, 'exampleId', 'Hello, World!')
        """
        element = self.wait_for_element(by, value)
        element.clear()
        element.send_keys(text)

    def click_element(self, by, value):
        """
        Waits for the presence of an element and then clicks it.

        Parameters:
            by: The method used to locate the element (e.g., By. ID, By.NAME, By.XPATH, etc.).
            value: The value of the method (e.g., the ID, name, or XPath expression).

        Usage:
            base_page.click_element(By.ID, 'exampleId')
        """
        element = self.wait_for_element(by, value)
        element.click()

    def navigate_to_url(self, url):
        """
        Navigates to the specified URL.

        Parameters:
            url (str): The URL to navigate to.
        """
        self.control.get(url)
        self.control.maximize_window()

    def capture_screenshot(self, filename):
        """
        Captures a screenshot of the current page and saves it to the specified filename.

        Parameters:
            filename (str): The filename (with path) to save the screenshot.

        Usage:
            base_page.capture_screenshot("path/to/screenshot.png")
        """
        self.control.get_screenshot_as_file(filename)

    def get_page_title(self):
        """
        Retrieves the title of the current page.

        Returns:
            str: The title of the current page.

        Usage:
            page_title = base_page.get_page_title()
        """
        return self.control.title

    def get_element_text(self,by,value):
        element = self.wait_for_element(by, value)
        return element.text

    def select_dropdown_option_by_value(self, by, value, option_value):
        """
        Waits for the presence of a dropdown element and selects an option by its value.

        Parameters:
            by: The method used to locate the dropdown element (e.g., By. ID, By.NAME, By.XPATH, etc.).
            value: The value of the method (e.g., the ID, name, or XPath expression) identifying the dropdown element.
            option_value: The value of the option to be selected.

        Usage:
            base_page.select_dropdown_option_by_value(By.ID, 'exampleDropdown', 'optionValue1')
        """
        element = self.wait_for_element(by, value)
        select = Select(element)
        select.select_by_value(option_value)

    def get_dropdown_options(self, by, value):
        """
        Retrieves the options available in a dropdown identified by the specified method and value.

        Parameters:
            by: The method used to locate the element (e.g., By. ID, By.NAME, By.XPATH, etc.).
            value: The value of the method (e.g., the ID, name, or XPath expression).

        Returns:
            List[str]: A list of text values representing the dropdown options.

        Usage:
            options = base_page.get_dropdown_options(By.ID, 'exampleDropdown')
        """
        element = self.wait_for_element(by, value)
        select = Select(element)
        tl = []
        for option in select.all_selected_options:
            tl.append(option.text)
        return tl
        #return [option.text for option in select.all_selected_options]

    def upload_file(self, by, value, file_path):
        """
        Uploads a file to the specified input element.

        Parameters:
            by: The method used to locate the input element (e.g., By. ID, By.NAME, By.XPATH, etc.).
            value: The value of the method (e.g., the ID, name, or XPath expression) identifying the input element.
            file_path: The path to the file to be uploaded.

        Usage:
            base_page.upload_file(By.ID, 'fileInput', '/path/to/file.txt')
        """
        element = self.wait_for_element(by, value)
        element.send_keys(file_path)


                   ### ALERT FUNCTIONS #####
    def wait_for_alert_to_be_present(self, timeout=10):
        """
        Waits for an alert to be present.

        Parameters:
            timeout (int): The maximum time to wait for the condition (default is 10 seconds).

        Usage:
            base_page.wait_for_alert_to_be_present(timeout=15)
        """
        return WebDriverWait(self.control, timeout).until(
            ec.alert_is_present()
        )

    def switch_to_alert(self):
        """
        Switches the focus to the current alert and returns the Alert object.

        Returns:
            Alert: The Alert object.

        Usage:
            alert = base_page.switch_to_alert()
        """
        return self.control.switch_to.alert

    def accept_alert(self):
        """
        Accepts the current alert.

        Usage:
            base_page.accept_alert()
        """
        alert = self.wait_for_alert_to_be_present()
        alert.accept()

    def get_alert_text(self):
        """
        Retrieves the text of the current alert.

        Returns:
            str: The text of the alert.

        Usage:
            alert_text = base_page.get_alert_text()
        """
        alert = self.wait_for_alert_to_be_present()
        return alert.text

    def wait_for_visible_element(self, by, value, timeout=10):
        """
        Waits for the visibility of an element identified by the specified method and value.

        Parameters:
            by: The method used to locate the element (e.g., By. ID, By.NAME, By.XPATH, etc.).
            value: The value of the method (e.g., the ID, name, or XPath expression).
            timeout (int): The maximum time to wait for the element to be visible (default is 10 seconds).

        Returns:
            WebElement: The located WebElement.

        Usage:
            element = base_page.wait_for_visible_element(By.ID, 'exampleId')
        """
        return WebDriverWait(self.control, timeout).until(ec.visibility_of_element_located((by, value)))

    def is_element_displayed(self, by, value):
        """
        Checks if an element identified by the specified method and value is displayed on the page.

        Parameters:
            by: The method used to locate the element (e.g., By. ID, By.NAME, By.XPATH, etc.).
            value: The value of the method (e.g., the ID, name, or XPath expression).

        Returns:
            bool: True if the element is displayed, False otherwise.

        Usage:
            is_displayed = base_page.is_element_displayed(By.ID, 'exampleId')
        """
        try:
            element = self.wait_for_visible_element(by, value)
            return element.is_displayed()
        except TimeoutException:
            return False


