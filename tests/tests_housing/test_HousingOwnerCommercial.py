import time

import pytest
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys

from pages.housing_pages.login_page import LoginPage
from pages.housing_pages.owner_commercia_page import OwnerCommercialPage
from tests.basetest import BaseTest
from tests.testdata import test_data_commercial
from tests.testdata.test_data_commercial import commercial
from utils.ConfigReaderUtil import ConfigReaderUtil


class Test_OwnerCommercial(BaseTest):
    def test_verifyCommercialRent(self):
        try:
            CommercialPage = OwnerCommercialPage(self.driver, self.filePath)
            logPage = LoginPage(self.driver, self.filePath)
            logPage.navigateToApplication(ConfigReaderUtil.get_env_value('baseUrl'))
            logPage.formAlert()
         #   logPage.getAllRole()
         #   logPage.getSubmitRole()
            CommercialPage.clickToCommercial()
            CommercialPage.rentIsEnable()
            CommercialPage.enterMobile(ConfigReaderUtil.get_env_value('userName'))
            CommercialPage.enterName(ConfigReaderUtil.get_env_value('passWord'))
            CommercialPage.clickToOffice()
           # CommercialPage.getCity(ConfigReaderUtil.get_env_value('City'))
           # CommercialPage.clickToCity()
            CommercialPage.clickOnStartNow()
            print("test")

        except WebDriverException as e:
            BaseTest.take_screenshot(self, e.msg)
            raise e

    def test_verifyCommercialSell(self):
        try:
            CommercialPage = OwnerCommercialPage(self.driver, self.filePath)
            logPage = LoginPage(self.driver, self.filePath)
            logPage.navigateToApplication(ConfigReaderUtil.get_env_value('baseUrl'))
            logPage.formAlert()
         #   logPage.getAllRole()
         #   logPage.getSubmitRole()
            CommercialPage.clickToCommercial()
            CommercialPage.clickSell()
            CommercialPage.enterMobile(ConfigReaderUtil.get_env_value('userName'))
            CommercialPage.enterName(ConfigReaderUtil.get_env_value('passWord'))
            CommercialPage.clickToOffice()
           # CommercialPage.getCity(ConfigReaderUtil.get_env_value('City'))
           # CommercialPage.clickToCity()
            CommercialPage.clickOnStartNow()
            print("test")

        except WebDriverException as e:
            BaseTest.take_screenshot(self, e.msg)
            raise e

    def test_propertDetailsProgress(self, getcommercialdata):
        self.test_verifyCommercialRent()
        CommercialPage = OwnerCommercialPage(self.driver, self.filePath)
        percentage = CommercialPage.scrollbarprogress().text
        actualPercentage = getcommercialdata["scrollbarprogress"][0]
        assert percentage == actualPercentage
        CommercialPage.enterBuilding(getcommercialdata["Building"])
        CommercialPage.eneterLocality(getcommercialdata["Locality"])
        CommercialPage.pressEnter()
        CommercialPage.selectReadyToMove()
        CommercialPage.selectAvailableDate()
        CommercialPage.clickDate()
        CommercialPage.enterPropertyAge(getcommercialdata["PropertyAge"])
        CommercialPage.selectPropertyZone()
        CommercialPage.selectPropertyHub()
        CommercialPage.selectPropertyCondition()
        CommercialPage.enterBuildUpArea(getcommercialdata["BuildUpArea"])
        CommercialPage.selectOwnership()
        CommercialPage.selectPropertyStat()
        CommercialPage.enterexpRent(getcommercialdata["Rent"][0])
        CommercialPage.enterFloors(getcommercialdata["Floor"])
        CommercialPage.floorarrow()
        elements_with_data_id = CommercialPage.getYourfloor()
        print(elements_with_data_id)
        data_ids = [element.get_attribute("data-id") for element in elements_with_data_id]
        print("Data id =", data_ids)
        CommercialPage.selectFloor()
        CommercialPage.enterPassLift(getcommercialdata["GetliftPass"])
        CommercialPage.enterServiceLift(getcommercialdata["Getliftser"])
        CommercialPage.clickamminities()
        print("Done")

    @pytest.fixture(params=commercial.test_data)
    def getcommercialdata(self, request):
        return request.param


