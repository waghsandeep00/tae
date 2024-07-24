import pytest
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common import actions

from pages.housing_pages.login_page import LoginPage
from pages.housing_pages.residencial_page import ResidentialPage
from tests.basetest import BaseTest
from tests.testdata.test_data_commercial import commercial
from tests.testdata.test_data_login import login_data
from utils.ConfigReaderUtil import ConfigReaderUtil


class Test_SelectCity(BaseTest):

    """
    Test case - Enter text and Select value from suggestion
    """
    def test_selectcity(self, getlogindata):
        try:
            profilepage = ResidentialPage(self.driver, self.filePath)
            logPage = LoginPage(self.driver, self.filePath)
            logPage.navigateToApplication(ConfigReaderUtil.get_env_value('mainurl'))
            profilepage.clicdropdown()
            profilepage.entercity(getlogindata['enterpartialcity'])
            profilepage.selectcity()

        except WebDriverException as e:
            BaseTest.take_screenshot(self, e.msg)
            raise e

    """
        Test case - Get list of all cities and select value match with user inputs
    """
    def test_collectcity(self, getlogindata):
        self.test_selectcity(getlogindata)
        profilepage = ResidentialPage(self.driver, self.filePath)
        profilepage.entersearch()
        profilepage.collectciti(getlogindata['userinputcity'])

    @pytest.fixture(params=login_data.test_login_Data)
    def getlogindata(self, request):
        return request.param
