import json

import pytest
import requests
from selenium.common.exceptions import WebDriverException

from tests.basetest import BaseTest
from tests.testdata.test_data_login import login_data
from utils.ConfigReaderUtil import ConfigReaderUtil


class Test_update(BaseTest):
    def test_updateResourse(self, getlogindata):
        try:
            url = ConfigReaderUtil.get_env_value('posturl')
            file = open(getlogindata["userdetails"], 'r')
            json_input = file.read()
            request_json = json.loads(json_input)
            response = requests.post(url, request_json)

          #  print(response.content)

        except WebDriverException as e:
            BaseTest.take_screenshot(self, e.msg)
            raise e

    @pytest.fixture(params=login_data.test_apifilepath)
    def getlogindata(self, request):
        return request.param
