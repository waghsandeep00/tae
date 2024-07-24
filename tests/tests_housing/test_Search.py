import pytest
from selenium.common.exceptions import WebDriverException

from pages.housing_pages.base_page import BasePage
from pages.housing_pages.login_page import LoginPage
from pages.housing_pages.residencial_page import ResidentialPage
from tests.basetest import BaseTest
from tests.testdata.test_data_commercial import commercial
from tests.testdata.test_data_login import login_data
from tests.tests_housing.test_SelectCity import Test_SelectCity
from utils.ConfigReaderUtil import ConfigReaderUtil


class Test_Search(BaseTest):
    def test_searchcity(self, getlogindata):
        try:
            selectcity = Test_SelectCity()
            selectcity.test_selectcity(getlogindata)

        except WebDriverException as e:
            BaseTest.take_screenshot(self, e.msg)
            raise e

    @pytest.fixture(params=login_data.test_login_Data)
    def getlogindata(self, request):
        return request.param