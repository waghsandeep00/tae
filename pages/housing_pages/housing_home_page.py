from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from locators.housing_locators import home_page_locator
from pages.housing_pages.base_page import BasePage
from webdriver.WebdriverBasePage import WebdriverBasePage


class HousingHomePage(BasePage):
    def __init__(self, x, filepath):
        self.driver = x
        self.filepath = filepath
        self.locator = home_page_locator.HomePageLocator
        super().__init__(self.driver, self.filepath)

    def navigateToApplication(self, url):
        BasePage.navigateto(self, url)
        BasePage.page_has_loaded(self)
        return self

    def checkAlert(self):
        BasePage.isElementPresent(self, By.XPATH, self.locator)
    def clickToHowItWorks(self):
        BasePage.click(self, By.XPATH, self.locator.HOW_IT_WORKS)
        return self

    def clickToFaqs(self):
        BasePage.click(self, By.XPATH, self.locator.FAQS)
        return self

    def checkTestomonialDescription(self):
        return self.driver.find_element(By.XPATH, self.locator.TESTOMONIAL_DESCRIPTION).text

    def checkTestomonialCity(self):
        return self.driver.find_element(By.XPATH, self.locator.TESTIMOIAL_CITY).text

    def checkTestomonialPerson(self):
        return self.driver.find_element(By.XPATH, self.locator.TESTOMONIAL_PERSON).text

    def checkTestomonialDescriptionNext(self):
        return self.driver.find_element(By.XPATH, self.locator.TESTOMONIAL_DESCRIPTIONNEXT).text
        #return BasePage.gettext(self, By.XPATH, self.locator.TESTOMONIAL_DESCRIPTION).text
        # return self

    def checkTestomonialCityNext(self):
        return self.driver.find_element(By.XPATH, self.locator.TESTIMOIAL_CITYNEXT).text

    def checkTestomonialPersonNext(self):
        return self.driver.find_element(By.XPATH, self.locator.TESTOMONIAL_PERSONNEXT).text
