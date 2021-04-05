from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators import myaccount_page_locators

class MyAccountPage(BasePage):

    def __init__(self, x, filepath):
        self.driver = x
        self.filepath = filepath
        self.locators = myaccount_page_locators.MyAccountPageLocator
        super().__init__(x, filepath)

    def verifyMyAccountPage(self):
        if BasePage.isElementPresent(self, By.XPATH, self.locators.PAGETITLE):
            assert True, "Login To Application"
        else:
            assert False, "Error while Login To Application"
        return self

    def clickToSingOutButton(self):
        BasePage.click(self, By.LINK_TEXT, self.locators.LOGOUT)
