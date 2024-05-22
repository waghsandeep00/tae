import time

import pytest
import selenium.webdriver.support.wait as wait
from selenium.common.exceptions import WebDriverException, ElementNotVisibleException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select

from tests.testdata.test_data_login import login_data
from webdriver.logger_page import LoggerClass


class WebdriverBasePage(object):
    filepath = ""

    def __init__(self, x, filepath):
        self.driver = x

        self.filepath = filepath
        """description of class"""

    def navigateto(self, url):
        self.driver.get(url)

    def elementWaitCondition(self, byelement, byindentifier):
        self.web_driver_wait = wait.WebDriverWait(self.driver, 30)
        self.web_driver_wait.until(
            expected_conditions.presence_of_element_located((byelement, byindentifier)), "element is not present")

    def windowswait(self, byelement, byindentifier):
        self.web_driver_wait = wait.WebDriverWait(self.driver, 10)
        self.web_driver_wait.until(expected_conditions.number_of_windows_to_be(2))
        google_window_handle = self.driver.window_handles[-1]
        self.driver.switch_to.window(google_window_handle)

    def waitUntilAlertPresent(self):
        self.web_driver_wait = wait.WebDriverWait(self.driver, 30)
        self.web_driver_wait.until(
            expected_conditions.alert_is_present(), "element is not present")

    def entertext(self, byelement, byindentifier, mvalue):
        try:
            self.elementWaitCondition(byelement, byindentifier)
            element = self.driver.find_element(by=byelement, value=byindentifier)
            element.clear()
            element.send_keys(mvalue)
            LoggerClass.writeFile(self.filepath,
                                  "\nEnter value : " + byindentifier + " value :" + mvalue)
        except WebDriverException as e:
            LoggerClass.writeFile(self.filepath, "\n" + e.msg)
            raise e

    def enterinnewwindow(self, byelement, byindentifier, mvalue):
        try:
            self.windowswait(byelement, byindentifier)
            element = self.driver.find_element(by=byelement, value=byindentifier)
            element.clear()
            element.send_keys(mvalue)
            LoggerClass.writeFile(self.filepath,
                                  "\nEnter value : " + byindentifier + " value :" + mvalue)
        except WebDriverException as e:
            LoggerClass.writeFile(self.filepath, "\n" + e.msg)
            raise e

    def click(self, byelement, byindentifier):
        try:
            self.elementWaitCondition(byelement, byindentifier)
            element = self.driver.find_element(by=byelement, value=byindentifier)
            element.click()
            LoggerClass.writeFile(self.filepath,
                                  "\nClick to " + byindentifier)
        except WebDriverException as e:
            LoggerClass.writeFile(self.filepath, "\n" + e.msg)
            raise e

    def collectvalues(self, byelement, byindentifier):
        try:
            self.elementWaitCondition(byelement, byindentifier)
            element = self.driver.find_elements(by=byelement, value=byindentifier)
            for ele in element:
                print("Found roles:", ele.text)
                if ele.text == "Owner":
                    ele.click()
                    break
            LoggerClass.writeFile(self.filepath,
                              "\nSubmit to " + byindentifier)
        except WebDriverException as e:
            LoggerClass.writeFile(self.filepath, "\n" + e.msg)
            raise e

    def dropdownMatch(self, byelement, byindentifier, getlogindata):
        try:
            self.elementWaitCondition(byelement, byindentifier)
            element = self.driver.find_elements(by=byelement, value=byindentifier)
            for ele in element:
                print(ele.text)
                if ele.text == getlogindata['SelectBuilding']:
                    ele.click()
                    break
            LoggerClass.writeFile(self.filepath,
                              "\nSubmit to " + byindentifier)
        except WebDriverException as e:
            LoggerClass.writeFile(self.filepath, "\n" + e.msg)
            raise e

    def gettext(self, byelement, byindentifier):
        try:
            self.elementWaitCondition(byelement, byindentifier)
            ele = self.driver.find_element(by=byelement, value=byindentifier)
            LoggerClass.writeFile(self.filepath,
                                  "\ngettext to " + byindentifier)

        except WebDriverException as e:
            LoggerClass.writeFile(self.filepath, "\n" + e.msg)
            raise e

    def submit(self, byelement, byindentifier):
        try:
            self.elementWaitCondition(byelement, byindentifier)
            element = self.driver.find_element(by=byelement, value=byindentifier)
            element.submit()
            LoggerClass.writeFile(self.filepath,
                                  "\nSubmit to " + byindentifier)
        except WebDriverException as e:
            LoggerClass.writeFile(self.filepath, "\n" + e.msg)
            raise e

    def selectdropdownvaluebytext(self, byelement, byindentifier, mvalue):
        try:
            self.elementWaitCondition(byelement, byindentifier)
            element1 = self.driver.find_element(by=byelement, value=byindentifier)
            element = Select(element1)
            element.select_by_visible_text(mvalue)
            LoggerClass.writeFile(self.filepath,
                                  "\nSelected DropDown " + byindentifier + "And Value" + mvalue + "Selected")
        except WebDriverException as e:
            LoggerClass.writeFile(self.filepath, "\n" + e.msg)
            raise e

    def driverquit(self):
        self.driver.quit()

    def pressTab(self, byelement, byindentifier):
        element1 = self.driver.find_element(by=byelement, value=byindentifier)
        action = ActionChains(self.driver)
        element1.action.send_keys(Keys.TAB)

    def pressEnter(self, byelement, byindentifier):
        try:
            self.elementWaitCondition(byelement, byindentifier)
            element1 = self.driver.find_element(by=byelement, value=byindentifier)
            action = ActionChains(self.driver)
            # action.send_keys(Keys.ENTER), element1
            action.move_to_element(element1).click().perform()

            LoggerClass.writeFile(self.filepath,
                          "\nSelected DropDown " + byindentifier + "Selected")
        except WebDriverException as e:
            LoggerClass.writeFile(self.filepath, "\n" + e.msg)
            raise e

    def isElementPresent(self, byelement, byindentifier):
        try:
            self.elementWaitCondition(byelement, byindentifier)
            element = self.driver.find_element(by=byelement, value=byindentifier)
            element.click()

        except WebDriverException:
            pass

    def isElementEnabled(self, byelement, byindentifier):
        try:
            self.elementWaitCondition(byelement, byindentifier)
            isElementEnabled = self.driver.find_element(by=byelement, value=byindentifier).is_enabled()
            return isElementEnabled
        except WebDriverException as e:
            raise e

    def isDisplayed(self, byelement, byindentifier):
        try:
            isDisplayedStatus = False
            self.elementWaitCondition(byelement, byindentifier)
            isElementEnabled = self.driver.find_element(by=byelement, value=byindentifier).is_displayed()
            return isElementEnabled
        except WebDriverException as e:
            raise e

    def isAlertIsPresent(self):
        try:
            self.web_driver_wait.until(
                expected_conditions.alert_is_present(), "Alert is not present")

        except WebDriverException as e:
            raise e

    def selectDropDownValueByIndex(self, byelement, byindentifier, mvalue):
        try:
            self.elementWaitCondition(byelement, byindentifier)
            element1 = self.driver.find_element(by=byelement, value=byindentifier)
            element = Select(element1)
            element.select_by_index(mvalue)
            LoggerClass.writeFile(self.filepath,
                                  "\nSelected DropDown " + byindentifier + "And Value " + mvalue + "Selected")
        except WebDriverException as e:
            LoggerClass.writeFile(self.filepath, "\n" + e.msg)
            raise e

    def selectDropDownValueByVisibleText(self, byelement, byindentifier, mvalue):
        try:
            self.elementWaitCondition(byelement, byindentifier)
            element1 = self.driver.find_element(by=byelement, value=byindentifier)
            element = Select(element1)
            element.select_by_visible_text(mvalue)
            LoggerClass.writeFile(self.filepath,
                                  "\nSelected DropDown " + byindentifier + "And Value " + mvalue + "Selected")
        except WebDriverException as e:
            LoggerClass.writeFile(self.filepath, "\n" + e.msg)
            raise e

    def selectDropDownValueByValue(self, byelement, byindentifier, mvalue):
        try:
            self.elementWaitCondition(byelement, byindentifier)
            element1 = self.driver.find_element(by=byelement, value=byindentifier)
            element = Select(element1)
            element.select_by_value(mvalue)
            LoggerClass.writeFile(self.filepath,
                                  "\nSelected DropDown " + byindentifier + "And Value " + mvalue + "Selected")
        except WebDriverException as e:
            LoggerClass.writeFile(self.filepath, "\n" + e.msg)
            raise e

    def clickAndHold(self, byelement, byindentifier):
        try:
            self.elementWaitCondition(byelement, byindentifier)
            element = self.driver.find_element(by=byelement, value=byindentifier)
            actions = ActionChains(self.driver)
            actions.move_to_element(element).click().perform()
            LoggerClass.writeFile(self.filepath,
                                  "\nClick and Hold to " + byindentifier)
        except WebDriverException as e:
            LoggerClass.writeFile(self.filepath, "\n" + e.msg)
            raise e

    def contextClick(self, byelement, byindentifier):
        try:
            element = self.driver.find_element(by=byelement, value=byindentifier)
            actions = ActionChains(self.driver)
            actions.context_click(element).perform()
            LoggerClass.writeFile(self.filepath,
                                  "\nContext Click to " + byindentifier)
        except WebDriverException as e:
            LoggerClass.writeFile(self.filepath, "\n" + e.msg)
            raise e

    def doubleClick(self, byelement, byindentifier):
        try:
            element = self.driver.find_element(by=byelement, value=byindentifier)
            actions = ActionChains(self.driver)
            actions.double_click(element).perform()
            LoggerClass.writeFile(self.filepath,
                                  "\nDouble Click to " + byindentifier)
        except WebDriverException as e:
            LoggerClass.writeFile(self.filepath, "\n" + e.msg)
            raise e

    def dragAndDrop(self, sourcebyelement, sourcebyindentifier, targetbyelement,
                    targetbyindentifier):
        try:
            sourceelement = self.driver.find_element(by=sourcebyelement, value=sourcebyindentifier)
            targetelement = self.driver.find_element(by=targetbyelement, value=targetbyindentifier)
            actions = ActionChains(self.driver)
            actions.click_and_hold(sourceelement).move_to(targetelement).release()
            LoggerClass.writeFile(self.filepath,
                                  "\nDrag element " + sourcebyindentifier + "Drop Element " + targetbyindentifier)
        except WebDriverException as e:
            LoggerClass.writeFile(self.filepath, "\n" + e.msg)
            raise e

    def clickByActionClass(self, byelement, byindentifier):
        try:
            self.elementWaitCondition(byelement, byindentifier)
            element = self.driver.find_element(by=byelement, value=byindentifier)
            actions = ActionChains(self.driver)
            actions.click(element).perform()
            LoggerClass.writeFile(self.filepath,
                                  "\nClick to " + byindentifier)
        except WebDriverException as e:
            LoggerClass.writeFile(self.filepath, "\n" + e.msg)
            raise e

    def clickToElementByJavaScript(self, byelement, byindentifier):
        try:
            self.elementWaitCondition(byelement, byindentifier)
            element = self.driver.find_element(by=byelement, value=byindentifier)
            self.driver.execute_script("arguments[0].click();", element)
            LoggerClass.writeFile(self.filepath,
                                  "\nClick to " + byindentifier)
        except WebDriverException as e:
            LoggerClass.writeFile(self.filepath, "\n" + e.msg)
            raise e

    def scrollToView(self, byelement, byindentifier):
        try:
            self.elementWaitCondition(byelement, byindentifier)
            element = self.driver.find_element(by=byelement, value=byindentifier)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);", element)
            self.driver.execute_script("arguments[0].click();", element)
        except WebDriverException as e:
            raise e

    def deSelectDropDownValueByIndex(self, byelement, byindentifier, mvalue):
        try:
            self.elementWaitCondition(byelement, byindentifier)
            element1 = self.driver.find_element(by=byelement, value=byindentifier)
            element = Select(element1)
            element.deselect_by_index(mvalue)
            LoggerClass.writeFile(self.filepath,
                                  "\nSelected DropDown " + byindentifier + "And Value " + mvalue + "deselected")
        except WebDriverException as e:
            LoggerClass.writeFile(self.filepath, "\n" + e.msg)
            raise e

    def deSelectDropDownValueByVisibleText(self, byelement, byindentifier, mvalue):
        try:
            self.elementWaitCondition(byelement, byindentifier)
            element1 = self.driver.find_element(by=byelement, value=byindentifier)
            element = Select(element1)
            element.deselect_by_visible_text(mvalue)
            LoggerClass.writeFile(self.filepath,
                                  "\nSelected DropDown " + byindentifier + "And Value " + mvalue + "deselected")
        except WebDriverException as e:
            LoggerClass.writeFile(self.filepath, "\n" + e.msg)
            raise e

    def deSelectDropDownValueByValue(self, byelement, byindentifier, mvalue):
        try:
            self.elementWaitCondition(byelement, byindentifier)
            element1 = self.driver.find_element(by=byelement, value=byindentifier)
            element = Select(element1)
            element.deselect_by_value(mvalue)
            LoggerClass.writeFile(self.filepath,
                                  "\nSelected DropDown " + byindentifier + "And Value " + mvalue + "deselected")
        except WebDriverException as e:
            LoggerClass.writeFile(self.filepath, "\n" + e.msg)
            raise e

    def checkBox(self, byelement, byindentifier):
        try:
            self.elementWaitCondition(byelement, byindentifier)
            element1 = self.driver.find_element(by=byelement, value=byindentifier)
            if not element1.is_selected():
                element1.click()
            LoggerClass.writeFile(self.filepath,
                                  "\nSelected DropDown " + byindentifier + "Check box selected")
        except WebDriverException as e:
            LoggerClass.writeFile(self.filepath, "\n" + e.msg)
            raise e

    def back(self):
        self.driver.back()

    def page_has_loaded(self):
        for i in range(10):
            page_state = self.driver.execute_script('return document.readyState;')
            time.sleep(3)
            if(page_state == 'complete'):
                break

    @pytest.fixture(params=login_data.test_login_Data)
    def getlogindata(self, request):
        return request.param


