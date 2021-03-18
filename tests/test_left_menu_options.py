from .basetest import BaseTest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class TestLeftMenuOptions(BaseTest):

    def test_elements_menu_list(self):
        self.driver.get("https://demoqa.com/elements")
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".element-group:nth-child(1)")))
        menu_options = self.driver.find_elements(By.CSS_SELECTOR, ".element-group:nth-child(1) ul li")
        for i in menu_options:
            print(i.text)

    def test_form_menu_list(self):
        self.driver.get("https://demoqa.com/elements")
        WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".element-group:nth-child(1)")))
        menu_options = self.driver.find_elements(By.CSS_SELECTOR, ".element-group:nth-child(2) ul li")
        for i in menu_options:
            print(i.text)

    def test_alerts_frame_windows_menu_list(self):
        self.driver.get("https://demoqa.com/elements")
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".element-group:nth-child(1)")))
        menu_options = self.driver.find_elements(By.CSS_SELECTOR, ".element-group:nth-child(3) ul li")
        for i in menu_options:
            print(i.text)

    def test_widgets_menu_list(self):
        self.driver.get("https://demoqa.com/elements")
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".element-group:nth-child(1)")))
        menu_options = self.driver.find_elements(By.CSS_SELECTOR, ".element-group:nth-child(4) ul li")
        for i in menu_options:
            print(i.text)

    def test_interactions_menu_list(self):
        self.driver.get("https://demoqa.com/elements")
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".element-group:nth-child(1)")))
        menu_options = self.driver.find_elements(By.CSS_SELECTOR, ".element-group:nth-child(5) ul li")
        for i in menu_options:
            print(i.text)

    def test_book_store_application_menu_list(self):
        self.driver.get("https://demoqa.com/elements")
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".element-group:nth-child(1)")))
        menu_options = self.driver.find_elements(By.CSS_SELECTOR, ".element-group:nth-child(6) ul li")
        for i in menu_options:
            print(i.text)