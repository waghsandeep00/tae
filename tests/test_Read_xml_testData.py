import pytest
from selenium.common.exceptions import WebDriverException

from tests.basetest import BaseTest


# purpose: method will return test data in dictionary format
# Paramaters: get_XML_data(<Testcase name from file testdata.xml>)

class TestDataReadXML(BaseTest):

    def test_Case3(self):
        try:
            dataxml = self.get_XML_data('TestCase3')
            print(dataxml)
        except WebDriverException as e:
            BaseTest.take_screenshot(self, e.msg)
            raise e
