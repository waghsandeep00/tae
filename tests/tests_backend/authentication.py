import requests
import pytest
#import requests.HTTPBasicAuth from auth
from requests.auth import HTTPBasicAuth
from selenium.common.exceptions import WebDriverException

from tests.basetest import BaseTest
from tests.testdata.test_data_login import login_data
from utils.ConfigReaderUtil import ConfigReaderUtil


class Test_authentication(BaseTest):
    def test_basic_authe(self, getlogindata):
        try:
            response = requests.get(getlogindata["baseauthurl"],
                                    auth=HTTPBasicAuth(ConfigReaderUtil.get_env_value('baseauth_user'),
                                                       ConfigReaderUtil.get_env_value('baseauth_pass')))
          #  print(response.text)

        except WebDriverException as e:
            BaseTest.take_screenshot(self, e.msg)
            raise e

    def test_google_basic_authe(self, getlogindata ):
        try:
            response = requests.get(getlogindata["googleauthurl"],
                                    auth=HTTPBasicAuth(ConfigReaderUtil.get_env_value('gauth_user'),
                                                       ConfigReaderUtil.get_env_value('gauth_pass')))
           # print(response.text)

        except WebDriverException as e:
            BaseTest.take_screenshot(self, e.msg)
            raise e

    @pytest.fixture(params=login_data.test_apifilepath)
    def getlogindata(self, request):
        return request.param