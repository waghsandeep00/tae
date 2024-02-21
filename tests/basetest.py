import os
from datetime import datetime
import allure
import pytest
from webdriver.logger_page import LoggerClass


@pytest.mark.usefixtures("driver_get", "create_logger_file", "test_data", "test_XML_data")
class BaseTest:

    def getData(self, name):
        valid_data = self.data[name]
        return valid_data

    def get_XML_data(self, name):
        valid_data = self.data['env'][name]
        return valid_data


    def take_screenshot(self, exception):
        today = datetime.today()
        date = today.strftime("%d_%m_%Y")
        timestamp = today.strftime("%d_%m_%Y_%H_%M_%S")
        file_directory = os.path.dirname(os.path.abspath(__file__))
        parent_directory = os.path.dirname(file_directory) + "\\testresults\\" + date + "\\Screenshots\\"
        ojectLoggerClass = LoggerClass()
        ojectLoggerClass.take_screenshot(parent_directory+self.testCaseName+"_"+timestamp, self.driver)
        ojectLoggerClass.writeFile(self.filePath, "\nTest Case Failed" + exception)
        ojectLoggerClass.writeFile(self.filePath,
                                   "\n------------------------------------------------------------------")
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name='screenshot',
            attachment_type=allure.attachment_type.PNG)
