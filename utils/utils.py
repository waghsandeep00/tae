# CONSTANTS
import datetime
import os
import xml.etree.ElementTree as ET

class UtilFunctions(object):

    @staticmethod
    def compare_list(actual_list, expected_list):
        actual_list.sort()
        expected_list.sort()
        if actual_list == expected_list:
            return True
        else:
            return False

    @staticmethod
    def chk_val_list(actual_list, ele):
        if (ele in actual_list):
            return True
        else:
            return False

    '''Sort the list in ascending/descending order'''
    @staticmethod
    def sort_list(actual_list):
        '''Accending order'''
        actual_list.sort(reverse=False)
        '''descending order'''
        actual_list.sort(reverse=True)

    '''get date and time'''
    @staticmethod
    def getCurrentDateAndTime():
        currentDateTime = datetime.now()
        print(currentDateTime)
        today = datetime.date.today()
        yesterday = today - datetime.timedelta(days=1)
        tomorrow = today + datetime.timedelta(days=1)
        print('today is', today, 'tomorrow is', tomorrow, 'yesterday is', yesterday)

    '''save the screenshot'''
    @staticmethod
    def saveCreenshot(driver):
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        driver.save_screenshot('screenshot.png' % now)

