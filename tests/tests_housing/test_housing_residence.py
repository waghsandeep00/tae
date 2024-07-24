import pytest
from selenium.common.exceptions import WebDriverException
from pages.housing_pages.login_page import LoginPage
from pages.housing_pages.residencial_page import ResidentialPage
from tests.basetest import BaseTest
from tests.testdata.test_data_commercial import commercial
from tests.testdata.test_data_login import login_data
from utils.ConfigReaderUtil import ConfigReaderUtil


class Test_Residence(BaseTest):
    def test_verifyResidenceRent(self, getlogindata):
        try:
            profilepage = ResidentialPage(self.driver, self.filePath)
            logPage = LoginPage(self.driver, self.filePath)
            logPage.navigateToApplication(ConfigReaderUtil.get_env_value('baseUrl'))
            logPage.formAlert()
         #   logPage.getAllRole()
         #   logPage.getSubmitRole()
            profilepage.residentialButtonEnable()
            profilepage.rentButtonEnable()
            profilepage.getMobileNumber(getlogindata['uname'])
            profilepage.getName(getlogindata['userfullname'])
           # profilepage.getCITY(getlogindata['city'])
            profilepage.clickOnStartNow()

        except WebDriverException as e:
            BaseTest.take_screenshot(self, e.msg)
            raise e

    def test_verifyResidenceSell(self, getlogindata):
        try:
            profilepage = ResidentialPage(self.driver, self.filePath)
            logPage = LoginPage(self.driver, self.filePath)
            logPage.navigateToApplication(ConfigReaderUtil.get_env_value('baseUrl'))
            logPage.formAlert()
         #   logPage.getAllRole()
         #   logPage.getSubmitRole()
            profilepage.residentialButtonEnable()
            profilepage.clickSell()
            profilepage.getMobileNumber(getlogindata['uname'])
            profilepage.getName(getlogindata['userfullname'])
           # profilepage.getCITY(getlogindata['city'])
            profilepage.clickOnStartNow()

        except WebDriverException as e:
            BaseTest.take_screenshot(self, e.msg)
            raise e

    def test_PropertyDetailProgress(self, getlogindata):
        try:
            self.test_verifyResidenceRent(getlogindata)
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

    def test_addPropertyDetails(self, getlogindata):
        try:
            self.test_PropertyDetailProgress(getlogindata)
            profilepage = ResidentialPage(self.driver, self.filePath)
            profilepage.clickOnAppartment()
            profilepage.eneterBuiiding(getlogindata['Building'])
            profilepage.clickEnter()
       #     profilepage.eneterLocality(getlogindata['locality'])
       #     profilepage.pressEnter()
            profilepage.enterBHK()
            profilepage.enterBuildUpArea(getlogindata['Buildup'])
            profilepage.selectFurnishType()
            profilepage.selectCheckBox()
            profilepage.clickOnNext()
            print("test run succesfully")
        except WebDriverException as e:
            BaseTest.take_screenshot(self, e.msg)
            raise e

    def test_PropertyDetailsCompleted(self, getlogindata):
        try:
            self.test_addPropertyDetails(getlogindata)
            profilepage = ResidentialPage(self.driver, self.filePath)
            percentage = profilepage.scrollbarprogress()
            print("Before adding details " + percentage)
            assert (percentage == getlogindata['scrollbarprogress'])
            propertystatus = profilepage.verifycompletedlabel()
            assert propertystatus == getlogindata['PropertyCompletestatus']
            print("done")
        except WebDriverException as e:
            BaseTest.take_screenshot(self, e.msg)
            raise e

    def test_addPriceDetails(self, getlogindata):
        try:
            self.test_addPropertyDetails(getlogindata)
            profilepage = ResidentialPage(self.driver, self.filePath)
            profilepage.enterMonthlyRent(getlogindata["MonthRent"])
            profilepage.clickAvailableFrom()
            profilepage.clickSelectDate()
            profilepage.clickSecurityDeposite()
            print("Not clicking on Post property")

        except WebDriverException as e:
            BaseTest.take_screenshot(self, e.msg)
            raise e

    @pytest.fixture(params=login_data.test_login_Data)
    def getlogindata(self, request):
        return request.param
