from utils.ConfigReaderUtil import ConfigReaderUtil
from webdriver.load_driverpage import LoadDriver
from webdriver.logger_page import LoggerClass
from datetime import datetime
import pytest
from utils import utils
import os
import allure
import json
import xmltodict
import xml.etree.cElementTree as ET

today = datetime.today()
date = today.strftime("%d_%m_%Y")
timestamp = today.strftime("%d_%m_%Y_%H_%M_%S")


@pytest.fixture(scope="session")
def driver_get(request):
    objectLoadDriver = LoadDriver()
    ConfigReaderUtil.set_config()
    driver = objectLoadDriver.setupOptionBrowserMethod(ConfigReaderUtil.get_env_value('browserName'))
    session = request.node
    for item in session.items:
        cls = item.getparent(pytest.Class)
        setattr(cls.obj, "driver", driver)
    driver.maximize_window()
    yield
    driver.close()
    driver.quit()



@pytest.fixture
def create_logger_file(request):
    ojectLoggerClass = LoggerClass()
    strPath = ojectLoggerClass.create_folderandfilename(date, timestamp,
                                                        "Application details:" + ConfigReaderUtil.get_env_value(
                                                            'baseUrl') +
                                                        "\n"
                                                        "------------------------------------------------------------------")
    ojectLoggerClass.writeFile(strPath, "\nTest Case Name : " + request.node.originalname)
    request.cls.filePath = strPath
    request.cls.testCaseName = request.node.originalname


@pytest.fixture
def test_data(request):
    data = get_test_data('test_data.json')
    request.cls.data = data


def get_test_data(filename):
    folder_path = os.path.abspath(os.path.dirname(__file__))
    folder = os.path.join(folder_path, 'testdata')
    jsonfile = os.path.join(folder, filename)
    with open(jsonfile) as file:
        data = json.load(file)
    return data


@pytest.fixture
def test_XML_data(request):
    file = 'test_data.xml'
    folder_path = os.path.abspath(os.path.dirname(__file__))
    folder = os.path.join(folder_path, 'testdata')
    fileName = os.path.join(folder, file)
    data=xmltodict.parse(ET.tostring(ET.parse(fileName).getroot()))
    request.cls.data = data


@pytest.fixture
def test_loginMulUsers(request):
    params = request.param
    name = params["username"]
    pwd = params["pwd"]
    allure.attach(f"This is the parameter {params} passed by the test case")
    yield name, pwd


@pytest.fixture
def util():
    return utils.UtilFunctions


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        mode = 'a' if os.path.exists('failures') else 'w'
        try:
            with open('failures', mode) as f:
                if 'driver_get' in item.fixturenames:
                    web_driver = item.funcargs['driver_get']
        except Exception as e:
            print('Fail to take screen-shot: {}'.format(e))


def pytest_runtest_setup(item):
    print("setting up", item.originalname)


def pytest_runtest_teardown(item):
    print("Completing test case" + item.originalname)


