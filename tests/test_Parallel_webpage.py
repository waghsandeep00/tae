import pytest
from selenium import webdriver
import time
from tests.basetest import BaseTest

#To run below tests in parallel run below commands from terminal
#py.test tests/test_Parallel_webpage.py -n 3

#run tests in paralel having marker named <parallel> and execute in 3 parallel nodes
#>py.test -m parallel -n 3

class TestParallel(BaseTest):
    @pytest.mark.parallel
    def test_google(self):
        self.driver.get("http://www.google.com")
        time.sleep(5)
        assert self.driver.title=="Google"

    @pytest.mark.parallel
    def test_facebook(self):
        self.driver.get("http://www.facebook.com")
        time.sleep(5)
        assert self.driver.title=="Facebook – log in or sign up"

    @pytest.mark.parallel
    def test_rediff(self):
            self.driver.get("https://www.rediff.com/")
            time.sleep(5)
            assert self.driver.title=="Rediff.com: News | Rediffmail | Stock Quotes | Shopping"

