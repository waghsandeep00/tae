from selenium.webdriver.common.by import By

from locators.housing_locators import login_page_locators
from pages.housing_pages.base_page import BasePage


class loginprofile(BasePage):
    def __init__(self, x, filepath):
        self.driver = x
        self.filepath = filepath
        self.locator = login_page_locators.LoginPageLocator
        super().__init__(self.driver, self.filepath)

    def verifyUserName(self):
        return self.driver.find_element(By.XPATH, self.locator.NAME).text

    def verfyMobileNumber(self):
        return self.driver.find_element(By.XPATH, self.locator.MOBILENUMBER).text

    def verifyEmail(self):
        return self.driver.find_element(By.XPATH, self.locator.EMAILADDRESS).text
