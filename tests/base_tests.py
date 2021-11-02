import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures('driver')
class TestBase:


    def test_search_for_element(self):
        self.TapAction(By.ID,'search')
        self.driver.find_element_by_id('search').send_keys("'t Hoeksken")
        self.TapAction(By.ID,'cityName')
        map = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout[2]')
        assert map.is_displayed()


    def test_element_on_the_map(self):
        self.TapAction(By.ID,'search')
        self.driver.find_element_by_id('search').send_keys("'t Hoeksken")
        self.TapAction('cityName')
        element = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout[2]/android.widget.ImageView')
        assert element.is_displayed()

    def test_screen_scroll(self):
        touch = TouchAction(self.driver)
        touch.press(x=535, y=2022).move_to(x=535, y=56).release().perform()
        for x in range(5):
            touch = TouchAction(self.driver)
            touch.press(x=535, y=2022).move_to(x=535, y=56).release().perform()
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[14]').click()

    def test_find_element_and_go_back(self):
        touch = TouchAction(self.driver)
        for x in range(2):
            touch.press(x=508, y=2022).move_to(x=514, y=511).release().perform()
            self.driver.find_element_by_id('/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[8]/android.widget.TextView').click()
        mapelement = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout[2]')
        assert mapelement.is_displayed()

    def test_scroll_to_specific_element(self):

        self.driver.find_element_by_android_uiautomator("new UiScrollable(new UiSelector()).scrollIntoView(text(\"Actlzayanca de Hidalgo, MX\"))")
        self.driver.implicitly_wait(120)
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[7]/android.widget.TextView').click()
        mapelement = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout[2]/android.widget.ImageView')
        assert mapelement.is_displayed()
