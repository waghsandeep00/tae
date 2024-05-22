import pytest
from selenium.common.exceptions import WebDriverException

from pages.housing_pages.housing_loginprofile_page import loginprofile
from pages.housing_pages.login_page import LoginPage
from tests.basetest import BaseTest
from tests.testdata.test_data_login import login_data
from utils.ConfigReaderUtil import ConfigReaderUtil


class Test_login(BaseTest):
    @pytest.mark.xdist
    @pytest.mark.beforelogin
    def test_pagatitle(self):
        try:
            logPage = LoginPage(self.driver, self.filePath)
            logPage.navigateToApplication(ConfigReaderUtil.get_env_value('baseUrl'))
            titledata = login_data()
            pagetitle = self.driver.title
            print(pagetitle)
            assert titledata.test_pagetitle["Title"] in pagetitle
            print("Title Verified")

        except WebDriverException as e:
            BaseTest.take_screenshot(self, e.msg)
            raise e
# Back dated method not using now 13/03/2024

    @pytest.mark.beforelogin
    def test_role(self, getlogindata):
        try:
            logPage = LoginPage(self.driver, self.filePath)
            logPage.navigateToApplication(ConfigReaderUtil.get_env_value('baseUrl'))
            logPage.formAlert()
            roles = logPage.getAllRole()
            print("Collect the roles of application 'Owner' and Broker'")

        except WebDriverException as e:
            BaseTest.take_screenshot(self, e.msg)
            raise e

    @pytest.mark.beforelogin
    def test_goback(self, getlogindata):
        try:
            logPage = LoginPage(self.driver, self.filePath)
            self.test_role(getlogindata)
            logPage.clickToLginHere()
            print("Login page navigation verified")

        except WebDriverException as e:
            BaseTest.take_screenshot(self, e.msg)
            raise e

    # The flow changes if application so wont able to run the script
    @pytest.mark.order(5)
    def test_login(self, getlogindata):
        try:
            logPage = LoginPage(self.driver, self.filePath)
            logPage.navigateToApplication(ConfigReaderUtil.get_env_value('baseUrl'))
            logPage.formAlert()
            logPage.clickToLginHere()
            logPage.enterUserName(getlogindata["uname"])
            logPage.clickToContinue()
            logPage.enterPassword(getlogindata["pass"])
            logPage.clickToSubmit()
            print("Login page verified by taking test data from fixture method")

        except WebDriverException as e:
            BaseTest.take_screenshot(self, e.msg)
            raise e
    # facing google security so wont able to run script

    @pytest.mark.order(5)
    @pytest.mark.parametrize("test_loginMulUsers", [
        {"username": "9552312095", "pwd": "Tiger@0073"},
        {"username": "9552312095", "pwd": "Tiger@7300"}], indirect=True)
    # This parameter we can take from fixture
    def test_loginWithMulUsers(self, test_loginMulUsers):
        try:
            name, pwd = test_loginMulUsers
            logPage = LoginPage(self.driver, self.filePath)
            logPage.navigateToApplication(ConfigReaderUtil.get_env_value('baseUrl'))
            logPage.formAlert()
            logPage.clickToLginHere()
            logPage.enterUserName(name)
            logPage.clickToContinue()
            logPage.enterPassword(pwd)
            logPage.clickToSubmit()
            print("Login page verified by taking multiple users data")
        except WebDriverException as e:
            BaseTest.take_screenshot(self, e.msg)
            raise e

    def test_loginWithConfig(self):
        try:
            logPage = LoginPage(self.driver, self.filePath)
            logPage.navigateToApplication(ConfigReaderUtil.get_env_value('baseUrl'))
    #        logPage.formAlert()
            logPage.clickToLginHere()
            logPage.enterUserName(ConfigReaderUtil.get_env_value('userName'))
            logPage.clickToContinue()
            logPage.enterPassword(ConfigReaderUtil.get_env_value('passWord'))
            logPage.clickToSubmit()
            print("Login page verified by taking test data from config file")

        except WebDriverException as e:
            BaseTest.take_screenshot(self, e.msg)
            raise e

    def test_verifyprofile(self, getlogindata):
        try:
            self.test_login(getlogindata)
            profilePageObject = loginprofile(self.driver, self.filePath)
            verifyname = profilePageObject.verifyUserName()
            assert (getlogindata["userfullname"] in verifyname)
            verifymonumber = profilePageObject.verfyMobileNumber()
            assert (getlogindata["uname"] in verifymonumber)
            verifyemail = profilePageObject.verifyEmail()
            assert (getlogindata["Email"] in verifyemail)
            print("After login verified the user profile data")

        except WebDriverException as e:
            BaseTest.take_screenshot(self, e.msg)
            raise e

    def test_signinwithgmail(self):
        try:
            logPage = LoginPage(self.driver, self.filePath)
            logPage.navigateToApplication(ConfigReaderUtil.get_env_value('baseUrl'))
            logPage.clickBroker()
            logPage.clickToGmailButton()
            logPage.enterEmail(ConfigReaderUtil.get_env_value('email'))
            logPage.clickNext()
        #    logPage.enterPassword(ConfigReaderUtil.get_env_value('passWord'))
            print("Login with gmail by switching window verified")
        except WebDriverException as e:
            BaseTest.take_screenshot(self, e.msg)
            raise e

    @pytest.fixture(params=login_data.test_login_Data)
    def getlogindata(self, request):
        return request.param
