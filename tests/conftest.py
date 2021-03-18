from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import pytest
from utils import utils
import os
import allure


@pytest.fixture(scope="session")
def driver_get(request):
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    session = request.node
    for item in session.items:
        cls = item.getparent(pytest.Class)
        setattr(cls.obj,"driver",driver)
    yield
    driver.quit()


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
                else:
                    print('Fail to take screen-shot')
                    return
            allure.attach(
                web_driver.get_screenshot_as_png(),
                name='screenshot',
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            print('Fail to take screen-shot: {}'.format(e))

def pytest_runtest_setup(item):
    print("setting up", item.originalname)

def pytest_runtest_teardown(item):
    print("Completing test case" + item.originalname)