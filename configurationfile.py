from appium import webdriver


def setup_driver():
    app_name = 'app-debug.apk'
    app_path = '/Users/michalzych/PycharmProjects/PythonAppiumMapProject/app-debug.apk'

    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['appname'] = app_name
    desired_caps['app'] = app_path
    desired_caps['newCommandTimeout'] = 120

    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    driver.implicitly_wait(30)
    return driver










