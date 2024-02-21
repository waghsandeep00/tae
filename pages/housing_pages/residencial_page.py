from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators.housing_locators import residence_page_locators
from pages.housing_pages.base_page import BasePage


class ResidentialPage(BasePage):
    def __init__(self, x, filepath):
        self.driver = x
        self.filepath = filepath
        self.locator = residence_page_locators.ResidencePageLocators()
        super().__init__(self.driver, self.filepath)

    def residentialButtonEnable(self):
        BasePage.isElementEnabled(self, By.XPATH, self.locator.RESIDENTIALBUTTON)
        return self

    def rentButtonEnable(self):
        BasePage.isElementEnabled(self, By.XPATH, self.locator.RENT)
        return self

    def getMobileNumber(self, mobile):
        BasePage.entertext(self, By.XPATH, self.locator.ENTER_MOBILE, mobile)
        return self

    def getName(self, name):
        BasePage.entertext(self, By.XPATH, self.locator.ENTER_NAME, name)
        return self

    def getCITY(self, city):
        BasePage.deSelectDropDownValueByVisibleText(self, By.XPATH, self.locator.SELECT_CITY, city)
        return self

    def clickOnStartNow(self):
        BasePage.scrollToView(self, By.XPATH, self.locator.START_NOW)
        return self

    def scrollbarprogress(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(self.locator.SCROLL_BAR)).text
        return element
        #return self.driver.find_element(By.XPATH, self.locator.SCROLL_BAR).text

    def clickOnAppartment(self):
        BasePage.click(self, By.XPATH, self.locator.APARTMENT)
        return self
