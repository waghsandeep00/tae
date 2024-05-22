from selenium.webdriver.common.by import By
from locators.housing_locators import login_page_locators
from pages.housing_pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, x, filepath):
        self.driver = x
        self.filepath = filepath
        self.locator = login_page_locators.LoginPageLocator
        super().__init__(self.driver, self.filepath)

    def navigateToApplication(self, url):
        BasePage.navigateto(self, url)
        BasePage.page_has_loaded(self)
        return self

    def clickBroker(self):
        BasePage.click(self, By.XPATH, self.locator.BROKER)
        return self

    def clickToGmailButton(self):
        BasePage.pressEnter(self, By.CSS_SELECTOR, self.locator.SIGNWITHGMAIL)
        return self

    def enterEmail(self, email):
        BasePage.enterinnewwindow(self, By.CSS_SELECTOR, self.locator.EMAIL, email)
        return self

    def clickNext(self):
        BasePage.click(self, By.XPATH, self.locator.NEXT)
        return self

    def enterPassword(self, passw):
        BasePage.enterinnewwindow(self, By.XPATH, self.locator.PASSWORD, passw)
        return self


    def formAlert(self):
        BasePage.isElementPresent(self, By.XPATH, self.locator.STUCK_IN_FORM_ALERT)
        return self

    def getAllRole(self):
        BasePage.collectvalues(self, By.XPATH, self.locator.COLLECT_ROLE)
        return self

    def getSelectRole(self):
        BasePage.click(self, By.XPATH, self.locator.SELECT_ROLE)
        return self

    def getGoBack(self):
        BasePage.click(self, By.XPATH, self.locator.GO_BACK)
        return self

    def getSubmitRole(self):
        BasePage.click(self, By.XPATH, self.locator.SUBMIT_ROLE)
        return self

    def clickToLginHere(self):
        BasePage.scrollToView(self, By.XPATH, self.locator.LOGINHERE)
       # BasePage.click(self, By.XPATH, self.locator.LOGINHERE)
        return

    def enterUserName(self, username):
        BasePage.entertext(self, By.XPATH, self.locator.USERNAME, username)
        return self

    def clickToContinue(self):
        BasePage.click(self, By.XPATH, self.locator.CONTINUE)
        return self

    def enterPassword(self, password):
        BasePage.entertext(self, By.XPATH, self.locator.PASSWORD, password)
        return self

    def clickToSubmit(self):
        BasePage.click(self, By.XPATH, self.locator.SUBMIT)
        return self





