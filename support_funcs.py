from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:

    def __init__(self,driver: webdriver.Remote):
        self.driver = driver

    def TapAction(self,selection_str,selection_val):
        element = self.driver.find_element(selection_val,selection_str)
        actions = TouchAction(self.driver)
        actions.tap(element)
        actions.perform()

    def wait_for_visibility_of_element(self,locator):
        element = WebDriverWait(self.driver,30).until(expected_conditions.visibility_of_element_located(locator))
        return element