from selenium.webdriver.support.ui import WebDriverWait
from webdriver.WebdriverBasePage import WebdriverBasePage


class BasePage(WebdriverBasePage):

    def __init__(self, driver, filepath):
        self.driver = driver
        self.filepath = filepath
        super().__init__(self.driver, self.filepath)

