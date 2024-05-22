from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.housing_locators import ownerCommercial_page_locators
from pages.housing_pages.base_page import BasePage


class OwnerCommercialPage(BasePage):
    def __init__(self, x, filepath):
        self.driver = x
        self.filepath = filepath
        self.locator = ownerCommercial_page_locators.OwnerCommercialPageLocators
        super().__init__(self.driver, self.filepath)

    def clickToCommercial(self):
        BasePage.click(self, By.XPATH, self.locator.LOGIN_WITH_OWNER_COMMERCIAL)
        return self

    def clickToOffice(self):
        BasePage.click(self, By.XPATH, self.locator.PROPERTY_LABEL)
        return self

    def rentIsEnable(self):
        BasePage.isElementEnabled(self, By.XPATH, self.locator.RENT)
        return self

    def clickSell(self):
        BasePage.click(self, By.XPATH, self.locator.SELL)
        return self

    def enterMobile(self, mobile):
        BasePage.entertext(self, By.XPATH, self.locator.ENTER_MOBILE, mobile)
        return self

    def enterName(self, name):
        BasePage.entertext(self, By.XPATH, self.locator.ENTER_NAME, name)
        return self

    def getCity(self, city):
        BasePage.entertext(self, By.XPATH, self.locator.SELECT_CITY, city)
        return self

    def clickToCity(self):
        BasePage.click(self, By.XPATH, self.locator.SELCT_CITYPU)
        return self

    def clickOnStartNow(self):
        BasePage.click(self, By.XPATH, self.locator.START_NOW)
        return self

    def scrollbarprogress(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(self.locator.SCROLL_BAR))
        return element
       # return self.driver.find_element(By.XPATH, self.locator.SCROLL_BAR).text

    def enterBuilding(self, build):
        BasePage.entertext(self, By.XPATH, self.locator.BUILDING, build)
        return self

    def eneterLocality(self, loca):
        BasePage.entertext(self, By.XPATH, self.locator.LOCALITY, loca)
        return self

    def pressEnter(self):
        BasePage.pressEnter(self, By.XPATH, self.locator.MOVETOLOCALITY)
        return self



    def selectReadyToMove(self):
        BasePage.scrollToView(self, By.XPATH, self.locator.READY_TO_MOVE)
        return self

    def selectAvailableDate(self):
        BasePage.click(self, By.XPATH, self.locator.AVAILABLE_DATE)
        return self

    def clickDate(self):
        BasePage.click(self, By.XPATH, self.locator.SELECT_DATE)
        return self

    def enterPropertyAge(self, age):
        BasePage.entertext(self, By.XPATH, self.locator.PROPERTY_AGE, age)
        return self

    def selectPropertyZone(self):
        BasePage.click(self, By.XPATH, self.locator.PROPERTY_ZONE)
        return self

    def selectPropertyHub(self):
        BasePage.click(self, By.XPATH, self.locator.PROPERTY_HUB)
        return self

    def selectPropertyCondition(self):
        BasePage.click(self, By.XPATH, self.locator.PROPERTY_CONDITION)
        return self

    def enterBuildUpArea(self, area):
        BasePage.entertext(self, By.XPATH, self.locator.BUIlt_UP, area)
        return self

    def selectOwnership(self):
        BasePage.click(self, By.XPATH, self.locator.OWNERSHIP)
        return self

    def selectPropertyStat(self):
        BasePage.click(self, By.XPATH, self.locator.CONSTRUCTION_STATUS)
        return self

    def enterexpRent(self, rent):
        BasePage.entertext(self, By.XPATH, self.locator.EXPECTED_RENT, rent)
        return self

    def enterFloors(self, floor):
        BasePage.entertext(self, By.XPATH, self.locator.TOTAL_FLOR, floor)
        return self

    def floorarrow(self):
        BasePage.click(self, By.XPATH, self.locator.YOURFLORARROW)
        return self

    def getYourfloor(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_all_elements_located(self.locator.YOUR_FLOR))
        return element

    def selectFloor(self):
        BasePage.click(self, By.XPATH, self.locator.SELECT_Flor)
        return self


    def enterPassLift(self, plist):
        BasePage.entertext(self, By.XPATH, self.locator.PASSENGERS_LIFT, plist)
        return self

    def enterServiceLift(self, slift):
        BasePage.entertext(self, By.XPATH, self.locator.SERVICE_LIFT, slift)
        return self

    def clickamminities(self):
        BasePage.click(self, By.XPATH, self.locator.NEXTTOAMMETIES)
        return self
