import pytest
from selenium.common.exceptions import WebDriverException
from pages.housing_pages.housing_home_page import HousingHomePage
from pages.housing_pages.login_page import LoginPage
from tests.basetest import BaseTest
from tests.testdata import test_data_homepage
from utils.ConfigReaderUtil import ConfigReaderUtil


class TestWeb(BaseTest):

    @pytest.mark.parametrize("test_loginMulUsers", [
        {"username": "Test7User7@qa.com", "pwd": "Admin1"},
        {"username": "Test7User7@qa.com", "pwd": "Admin2"}], indirect=True)
    def test_howitworks(self, test_loginMulUsers):
        try:
            HomePageObject = HousingHomePage(self.driver, self.filePath)
            HomePageObject.navigateToApplication(ConfigReaderUtil.get_env_value('baseUrl'))
            HomePageObject.clickToHowItWorks()
            print("Navigation verified")

        except WebDriverException as e:
            BaseTest.take_screenshot(self, e.msg)
            raise e

    def test_faqs(self):
        try:
            HomePageObject = HousingHomePage(self.driver, self.filePath)
            HomePageObject.navigateToApplication(ConfigReaderUtil.get_env_value('baseUrl'))
            description = HomePageObject.clickToFaqs()
            print("Navigation verified")

        except WebDriverException as e:
            BaseTest.take_screenshot(self, e.msg)
            raise e

    def test_testmonial(self, homepagetestdata):
        try:
            HomePageObject = HousingHomePage(self.driver, self.filePath)
            HomePageObject.navigateToApplication(ConfigReaderUtil.get_env_value('baseUrl'))
            description = HomePageObject.checkTestomonialDescription()
            assert description == homepagetestdata["Description1"]
            city = HomePageObject.checkTestomonialCity()
            assert city == homepagetestdata["City1"]
            person = HomePageObject.checkTestomonialPerson()
            assert person == homepagetestdata["Person1"]
            print("Testimonial verified")

        except WebDriverException as e:
            BaseTest.take_screenshot(self, e.msg)
            raise e

    def test_testmonialsecond(self, homepagetestdata):
        try:
            HomePageObject = HousingHomePage(self.driver, self.filePath)
            HomePageObject.navigateToApplication(ConfigReaderUtil.get_env_value('baseUrl'))
            logPage = LoginPage(self.driver, self.filePath)
            logPage.formAlert()
            description = HomePageObject.checkTestomonialDescriptionNext()
            assert description == homepagetestdata["Description2"]
            city = HomePageObject.checkTestomonialCityNext()
            assert city == homepagetestdata["City2"]
            person = HomePageObject.checkTestomonialPersonNext()
            assert person == homepagetestdata["Person2"]
            print("Testimonial verified")

        except WebDriverException as e:
            BaseTest.take_screenshot(self, e.msg)
            raise e

    @pytest.fixture(params=test_data_homepage.homepagedata.test_testmonial_Data)
    def homepagetestdata(self, request):
        return request.param