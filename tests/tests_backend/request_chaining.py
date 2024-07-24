import jsonpath
import pytest
import requests
import json
from selenium.common.exceptions import WebDriverException
from utils.ConfigReaderUtil import ConfigReaderUtil
from tests.basetest import BaseTest
from tests.testdata.test_data_login import login_data
#Scenario- Adding new user and by using id of created resourse get the details called request chaining

class Test_requestchaining(BaseTest):
    def test_add_user(self):
        try:
            global store_id
            API_URL = ConfigReaderUtil.get_env_value('add')
            jsondata_file = open(getlogindata["userdetails"], 'r')
            json_request = json.loads(jsondata_file.read())
            response = requests.post(API_URL, json_request)
            print("Added user " + response.text)
            store_id = jsonpath.jsonpath(response.json(), 'id')
            print(store_id[0])
        except WebDriverException as e:
            BaseTest.take_screenshot(self, e.msg)
            raise e


    def test_getusetdetails(self):
        try:
            API_URL = "https://thetestingworldapi.com/api/studentsDetails"
            jsondata_file = open('C:\\Users\\sandeep.wagh\\Documents\\API test data\\end_to_end_postrequest.json', 'r')
            json_request = json.loads(jsondata_file.read())
            response = requests.post(API_URL, json_request)
            store_id = jsonpath.jsonpath(response.json(), 'id')
            finalgetstudentdetail = "https://thetestingworldapi.com/api/FinalStudentDetails/" + str(store_id[0])
            response = requests.get(finalgetstudentdetail)
            print("The user details is " + response.text)
        except WebDriverException as e:
            BaseTest.take_screenshot(self, e.msg)
            raise e

    @pytest.fixture(params=login_data.test_apifilepath)
    def getlogindata(self, request):
        return request.param
