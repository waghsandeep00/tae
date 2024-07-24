import json
import pytest
import jsonpath
import requests
from selenium.common.exceptions import WebDriverException

from tests.basetest import BaseTest
from tests.testdata.test_data_login import login_data
from utils.ConfigReaderUtil import ConfigReaderUtil


class Test_Add(BaseTest):
    def test_endtoend(self, getlogindata):
        try:
            API_URL = ConfigReaderUtil.get_env_value('add')
            jsondata_file = open(getlogindata["userdetails"], 'r')
            json_request = json.loads(jsondata_file.read())
            response = requests.post(API_URL, json_request)
            # print(response.text)
            store_id = jsonpath.jsonpath(response.json(), 'id')
            # print(store_id[0])

            techdetail_addurl = ConfigReaderUtil.get_env_value('addtechdetails')
            jsondata_file = open(getlogindata["tehcdetails"], 'r')
            json_request = json.loads(jsondata_file.read())
            # print(json_request)
            stid = json_request["st_id"]
            # print(stid)
            json_request['id'] = int(store_id[0])
            json_request['st_id'] = (store_id[0])
            response = requests.post(techdetail_addurl, json_request)
            # print(response.text)

            address_addurl = ConfigReaderUtil.get_env_value('address')
            jsondata_file = open(getlogindata["adddetails"], 'r')
            json_request = json.loads(jsondata_file.read())
            response = requests.post(address_addurl, json_request)
            json_request['stId'] = (store_id[0])
           #  print(response.text)

            finalgetstudentdetail = ConfigReaderUtil.get_env_value('finaldetails') + str(store_id[0])
            response = requests.get(finalgetstudentdetail)
           #  print(response.text)
          #   print("done")

        except WebDriverException as e:
            BaseTest.take_screenshot(self, e.msg)
            raise e

        # scenario - Add technical details for added user by taking same id

    def test_deleterequest(self, getlogindata):
        try:
            url = ConfigReaderUtil.get_env_value('delete')

            response = requests.delete(url)
            assert getlogindata["deleteresponse"] == response

        except WebDriverException as e:
            BaseTest.take_screenshot(self, e.msg)
            raise e

    @pytest.fixture(params=login_data.test_apifilepath)
    def getlogindata(self, request):
        return request.param
