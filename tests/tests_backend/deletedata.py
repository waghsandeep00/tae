import requests
import pytest
import json
import jsonpath
from selenium.common.exceptions import WebDriverException

from tests.basetest import BaseTest
from tests.testdata.test_data_login import login_data


class Test_delete(BaseTest):
    def test_deleterequest(self, getlogindata):
        try:
            url = getlogindata["deleteurl"]

            response = requests.delete(url)

        except WebDriverException as e:
            BaseTest.take_screenshot(self, e.msg)
            raise e

    @pytest.fixture(params=login_data.test_apifilepath)
    def getlogindata(self, request):
        return request.param

