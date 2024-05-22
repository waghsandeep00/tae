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

    def clickSell(self):
        BasePage.click(self, By.XPATH, self.locator.SELL)
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

    def eneterBuiiding(self, build):
        BasePage.entertext(self, By.XPATH, self.locator.BUILDING, build)
        return self

    def clickEnter(self):
        BasePage.pressEnter(self, By.XPATH, self.locator.MOVETOBUILDING)
        return self

    def eneterLocality(self, loca):
        BasePage.entertext(self, By.XPATH, self.locator.LOCALITY, loca)
        return self

    def pressEnter(self):
        BasePage.pressEnter(self, By.XPATH, self.locator.MOVETOLOCALITY)
        return self

    def enterBHK(self):
        BasePage.click(self, By.XPATH, self.locator.BHK)
        return self

    def enterBuildUpArea(self, area):
        BasePage.entertext(self, By.XPATH, self.locator.BUILDUP, area)
        return self

    def selectFurnishType(self):
        BasePage.click(self, By.XPATH, self.locator.FURNISHTYPE)

    def selectCheckBox(self):
        BasePage.checkBox(self, By.XPATH, self.locator.CHECKBOX)
        return self

    def clickOnNext(self):
        BasePage.click(self, By.XPATH, self.locator.NEXTBUTTON)
        return self

    def verifycompletedlabel(self):
        return self.driver.find_element(By.XPATH, self.locator.PROPERTYCOMPLETED).text

    def enterMonthlyRent(self, monthrent):
        BasePage.entertext(self, By.XPATH, self.locator.MONTHLYRENT, monthrent)
        return self

    def clickAvailableFrom(self):
        BasePage.click(self, By.XPATH, self.locator.AVAILABLEFROM)
        return self

    def clickSelectDate(self):
        BasePage.click(self, By.XPATH, self.locator.DATE)
        return self

    def clickSecurityDeposite(self):
        BasePage.click(self, By.XPATH, self.locator.SECURITYDEPOSIT)
        return self
