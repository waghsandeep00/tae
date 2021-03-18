import pytest
from selenium.webdriver.support.ui import WebDriverWait

@pytest.mark.usefixtures("driver_get")
class BaseTest:
    pass
