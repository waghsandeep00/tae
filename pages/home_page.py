"""
This module keeps home page POM
"""
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators import home_page_locators
from .base_page import BasePage


class HomePage(BasePage): # pylint: disable=too-few-public-methods
    """
    Home page class.
    """

    def __init__(self, driver):
        '''
        Home page constructor. Expects driver as parameter.
        '''
        self.locator = home_page_locators.HomePageLocator
        super().__init__(driver)

        self._helping_options = self.driver.find_elements\
            (By.CSS_SELECTOR,self.locator.HELPING_OPTIONS)

    def get_all_helping_options(self):
        """
        This function returns all helping options as list.
        """
        self.web_driver_wait.until(EC.presence_of_element_located
                                   ((By.CSS_SELECTOR,self.locator.FOOTER)))
        data = []
        for i in self._helping_options:
            data.append(i.text)
        return data
