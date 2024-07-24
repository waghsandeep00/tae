import jsonpath
import pytest
import requests
import json

from selenium.common.exceptions import WebDriverException

from tests.testdata.test_data_login import login_data
from utils.ConfigReaderUtil import ConfigReaderUtil
from tests.basetest import BaseTest


class Test_postrequest(BaseTest):
    def test_add_user(self, getlogindata):
        try:
            API_URL = ConfigReaderUtil.get_env_value('add')
            jsondata_file = open(getlogindata["userdetails"], 'r')
            json_request = json.loads(jsondata_file.read())
            response = requests.post(API_URL, json_request)
            print(response.text)

        except WebDriverException as e:
            BaseTest.take_screenshot(self, e.msg)
            raise e

    def test_get_user(self):
        try:
            API_URL = ConfigReaderUtil.get_env_value('add') + "/7549955"
            response = requests.get(API_URL)
            json_responce = json.loads(response.text)
            json_path = jsonpath.jsonpath(json_responce, 'data.id')
            print(json_path)
            assert json_path == [7549955]
            print(response.text)

        except WebDriverException as e:
            BaseTest.take_screenshot(self, e.msg)
            raise e

    @pytest.fixture(params=login_data.test_apifilepath)
    def getlogindata(self, request):
        return request.param
