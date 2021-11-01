import pytest
from appium import webdriver
#pytest rozpoznaje plik pod nazwą conftest jako plik setupowy

#fixture - klasa która powoduje że mój driver działa w obrębie wszystkich klas
@pytest.fixture(scope='class')
def driver(request):

    app_name = 'app-debug.apk'
    app_path = '/Users/michalzych/PycharmProjects/PythonAppiumMapProject/app-debug.apk'

    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['appname'] = app_name
    desired_caps['app'] = app_path
    desired_caps['newCommandTimeout'] = 120

    request.cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    request.cls.driver.implicitly_wait(30)
    return driver









