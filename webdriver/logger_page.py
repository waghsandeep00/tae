
import os
from datetime import datetime


class LoggerClass(object):

    @staticmethod
    def createFile(filename):
        file1 = open(filename, "x")
        file1.close()

    @staticmethod
    def writeFile(filename, message):
        file1 = open(filename, "a")
        file1.write(message)
        file1.close()

    def create_folderandfilename(self, date, timestamp, message):
        folder_path = os.path.abspath(os.path.dirname(__file__))
        finalfolderPath = os.path.join(folder_path.replace("\\webdriver", ""), 'testresults')
        folderpath = "{folder}\\{date}".format(
            folder=finalfolderPath,
            date=date
        )
        try:
            if not os.path.exists(folderpath):
                os.mkdir(folderpath)
                os.mkdir(folderpath + "\\Screenshots")
                os.mkdir(folderpath + "\\allure-reports")
                os.mkdir(folderpath + "\\allure-reportshtml")

            path = "{folder}\\{date}\\{timestamp}".format(
                folder=finalfolderPath,
                date=date,
                timestamp=timestamp
            )
            if not os.path.exists(path+".txt"):
                LoggerClass.createFile(path+".txt")
                LoggerClass.writeFile(path+".txt", message)

        except OSError:
            print("Creation of the directory %s failed" % path+".txt")
        return path+".txt"

    def take_screenshot(self, filePath, driver):
        filename = filePath + ".png"
        driver.get_screenshot_as_file(filename)
