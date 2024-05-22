import os

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

class EdgeOptions(object):
    pass

class LoadDriver(object):
    driver_folderpath = "null"

    def setupOptionBrowserMethod(self, argument, ini_location="\\drivers\\"):
        finalorg = argument.lower()
        self.driver_folderpath =ini_location
        file_directory = os.path.dirname(os.path.abspath(__file__))
        self.parent_directory = os.path.dirname(file_directory) + self.driver_folderpath
        if finalorg == 'chrome':
            argumentOption = 1
        elif finalorg == 'edge':
            argumentOption = 2
        elif finalorg == 'firefox':
            argumentOption = 3
        elif finalorg == 'edgechromium':
            argumentOption = 4
        else:
            argumentOption = 0
        switcher = {
            1: self.chrome,
            2: self.edge,
            3: self.firefox,
            4: self.edgechromium
        }
        fun = switcher.get(argumentOption, lambda: "Invalid Option")
        return fun()

    def chrome(self):
        #driverobject = webdriver.Chrome(executable_path= self.parent_directory +"\\chromedriver.exe");
        #driverobject = webdriver.Chrome(ChromeDriverManager().install())
        driverobject = webdriver.Edge(EdgeChromiumDriverManager().install())
        return driverobject

    def edge(self):
        # driverobject = webdriver.edge()
        driverobject=webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())
        return driverobject

    def firefox(self):
        # driverobject = webdriver.firefox()
        driverobject= webdriver.Firefox(executable_path=GeckoDriverManager().install())
        return driverobject

    def edgechromium(self):
        options = EdgeOptions()
        options.use_chromium = True
        options.binary_location = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

        driverobject = webdriver.Edge(
            executable_path=self.parent_directory +"\\msedgedriver.exe")
        return driverobject
