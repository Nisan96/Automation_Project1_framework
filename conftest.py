import pytest
from selenium import webdriver
from config.url_config import urlConfig
from config.browser_config import browserConfig

@pytest.fixture  ## Decorator called
def setup():
    if browserConfig.Browser == "Edge":
        drive = webdriver.Edge()
    elif browserConfig.Browser == "firefox":
        drive = webdriver.Firefox()
    elif browserConfig.Browser == "chrome":
        drive = webdriver.Chrome()
    else:
        raise ValueError("Unsupported browser:" + browserConfig.Browser)

    #drive.get(urlConfig.base_url)
    #drive.maximize_window()

    yield drive
    drive.quit()