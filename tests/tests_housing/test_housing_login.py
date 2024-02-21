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

    @pytest.mark.beforelogin
    def test_role(self, getlogindata):
        try:
            logPage = LoginPage(self.driver, self.filePath)
            logPage.navigateToApplication(ConfigReaderUtil.get_env_value('baseUrl'))
            logPage.formAlert()
            logPage.getAllRole()
            logPage.getSubmitRole()

        except WebDriverException as e:
            BaseTest.take_screenshot(self, e.msg)
            raise e

    @pytest.mark.beforelogin
    def test_goback(self, getlogindata):
        try:
            logPage = LoginPage(self.driver, self.filePath)
            self.test_role(getlogindata)
            logPage.getGoBack()
            print("Go to back url verified")

        except WebDriverException as e:
            BaseTest.take_screenshot(self, e.msg)
            raise e

    @pytest.mark.order(5)
    def test_formSubmission(self, getlogindata):
        try:
            logPage = LoginPage(self.driver, self.filePath)
            logPage.navigateToApplication(ConfigReaderUtil.get_env_value('baseUrl'))
    #        logPage.formAlert()
            logPage.clickOnLginHere()
            logPage.enterUserName(getlogindata["uname"])
            logPage.clickOnContinue()
            logPage.enterPassword(getlogindata["pass"])
            logPage.clickOnSubmit()

        except WebDriverException as e:
            BaseTest.take_screenshot(self, e.msg)
            raise e

    def test_verifyprofile(self, getlogindata):
        try:
            self.test_formSubmission(getlogindata)
            profilePageObject = loginprofile(self.driver, self.filePath)
            verifyname = profilePageObject.verifyUserName()
            assert (getlogindata["userfullname"] in verifyname)
            verifymonumber = profilePageObject.verfyMobileNumber()
            assert (getlogindata["uname"] in verifymonumber)
            verifyemail = profilePageObject.verifyEmail()
            assert (getlogindata["Email"] in verifyemail)

        except WebDriverException as e:
            BaseTest.take_screenshot(self, e.msg)
            raise e

    @pytest.fixture(params=login_data.test_login_Data)
    def getlogindata(self, request):
        return request.param
