import pytest
from selenium.common.exceptions import WebDriverException
from pages.housing_pages.login_page import LoginPage
from pages.housing_pages.residencial_page import ResidentialPage
from tests.basetest import BaseTest
from tests.testdata.test_data_login import login_data
from utils.ConfigReaderUtil import ConfigReaderUtil


class Test_Residence(BaseTest):
    def test_verifyresidence(self, getlogindata):
        try:
            profilepage = ResidentialPage(self.driver, self.filePath)
            logPage = LoginPage(self.driver, self.filePath)
            logPage.navigateToApplication(ConfigReaderUtil.get_env_value('baseUrl'))
            logPage.formAlert()
            logPage.getAllRole()
            logPage.getSubmitRole()
            profilepage.residentialButtonEnable()
            profilepage.rentButtonEnable()
            profilepage.getMobileNumber(getlogindata["uname"])
            profilepage.getName(getlogindata['userfullname'])
         #  profilepage.getCITY(getlogindata['city'])
            profilepage.clickOnStartNow()

        except WebDriverException as e:
            BaseTest.take_screenshot(self, e.msg)
            raise e

    def test_PropertyDetailProgress(self, getlogindata):
        try:
            self.test_verifyresidence(getlogindata)
            profilepage = ResidentialPage(self.driver, self.filePath)
            percentage = profilepage.scrollbarprogress()
            print("Before adding details " + percentage)
            assert (percentage == '5%')
            profilepage.clickOnAppartment()
            percentage = profilepage.scrollbarprogress()
            assert percentage == '10%'
            print("After adding details " + percentage)

        except WebDriverException as e:
            BaseTest.take_screenshot(self, e.msg)
            raise e

    @pytest.fixture(params=login_data.test_login_Data)
    def getlogindata(self, request):
        return request.param
