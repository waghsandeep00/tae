from selenium.webdriver.support.ui import WebDriverWait


class BasePage(object):
    def __init__(self, driver, timeout=30):
        self.driver = driver
        self.web_driver_wait = WebDriverWait(self.driver, 30)

    # def find_element(self, *locator):
    #     return self.driver.find_element(*locator)
    #
    # def find_elements(self, *locator):
    #     return self.driver.find_elements(*locator)
    #
    # def get_title(self):
    #     return self.driver.title
    #
    # def get_url(self):
    #     return self.driver.current_url
