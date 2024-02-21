import pytest
from selenium.common.exceptions import WebDriverException
from pages.housing_pages.login_page import LoginPage
from tests.basetest import BaseTest
from utils.ConfigReaderUtil import ConfigReaderUtil


class TestWeb(BaseTest):

    @pytest.mark.parametrize("test_loginMulUsers", [
        {"username": "Test7User7@qa.com", "pwd": "Admin1"},
        {"username": "Test7User7@qa.com", "pwd": "Admin2"}], indirect=True)
    def test_login(self, test_loginMulUsers):
        try:
            name, pwd = test_loginMulUsers
            loginPageObject = LoginPage(self.driver, self.filePath)
            loginPageObject.navigateToApplication(ConfigReaderUtil.get_env_value('baseUrl'))
            loginPageObject .clickToSingIn()
            loginPageObject.enterUserName(name)
            loginPageObject.enterPassword(pwd)
            myAccountPageObject = loginPageObject.clickToSingInButton()
            myAccountPageObject.verifyMyAccountPage()
            myAccountPageObject.clickToSingOutButton()
        except WebDriverException as e:
            BaseTest.take_screenshot(self, e.msg)
            raise e

    def test_loginwithConfig(self):
        try:
            loginPageObject = LoginPage(self.driver, self.filePath)
            loginPageObject.navigateToApplication(ConfigReaderUtil.get_env_value('baseUrl'))
            loginPageObject.clickToSingIn()
            loginPageObject.enterUserName(ConfigReaderUtil.get_env_value('userName'))
            loginPageObject.enterPassword(ConfigReaderUtil.get_env_value('passWord'))
            myAccountPageObject = loginPageObject.clickToSingInButton()
            myAccountPageObject.verifyMyAccountPage()
            myAccountPageObject.clickToSingOutButton()
        except WebDriverException as e:
            BaseTest.take_screenshot(self, e.msg)
            raise e

    def test_createAccount(self):
        try:
            finalData = self.getData('test_createAccount')  # enter your test case name
            loginPageObject = LoginPage(self.driver, self.filePath)
            loginPageObject.navigateToApplication(ConfigReaderUtil.get_env_value('baseUrl'))
            loginPageObject.clickToSingIn()
            loginPageObject.enterEmailAddress(finalData['Email'])
            createAccountPageObject = loginPageObject.clickToCreateAccount()
            createAccountPageObject.selectTitle(finalData['Title'])
            createAccountPageObject.enterFirstName(finalData['FirstName'])
            createAccountPageObject.enterLastName(finalData['LastName'])
            createAccountPageObject.enterPassword(finalData['Password'])
            createAccountPageObject.selectBirthDay(finalData['Birthday'])
            createAccountPageObject.selectBirthMonth(finalData['BirthMonth'])
            createAccountPageObject.selectBirthYear(finalData['BirthYear'])
            createAccountPageObject.checkNewsLetterCheckBox()
            createAccountPageObject.checkReceiveSpecialOffersCheckBox()
            createAccountPageObject.enterCompanyName(finalData['CompanyName'])
            createAccountPageObject.enterAddress1(finalData['Address1'])
            createAccountPageObject.enterAddress2(finalData['Address2'])
            createAccountPageObject.enterCity(finalData['City'])
            createAccountPageObject.selectState(finalData['State'])
            createAccountPageObject.enterPostCode(finalData['PostCode'])
            createAccountPageObject.selectCountry(finalData['Country'])
            createAccountPageObject.enterOtherInfo(finalData['OtherInfo'])
            createAccountPageObject.enterPhoneNumber(finalData['PhoneNumber'])
            createAccountPageObject.enterMobileNumber(finalData['MobileNumber'])
            myAccountPageObject = createAccountPageObject.clickToRegister()
            myAccountPageObject.verifyMyAccountPage()
            myAccountPageObject.clickToSingOutButton()
        except WebDriverException as e:
            BaseTest.take_screenshot(self, e.msg)
            raise e

