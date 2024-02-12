from selenium.common.exceptions import WebDriverException

from .basetest import BaseTest
from pages import home_page


class TestGoogle(BaseTest):

    def test_title(self):
        self.driver.get("https://demoqa.com/")
        assert self.driver.title == "DEMOQA"

    def test_helping_options(self, util):
        try:
            self.h_page = home_page.HomePage(self.driver, self.filepath)
            actual_options = self.h_page.get_all_helping_options()
            expected_options = ["Elements", "Forms", "Alerts, Frame & Windows", "Widgets", "Interactions",
                                "Book Store Application"]
            util.compare_list(actual_options, expected_options)
        except WebDriverException as e:
            BaseTest.take_screenshot(self, e.msg)
        raise e
