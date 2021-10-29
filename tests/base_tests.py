import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


@pytest.mark.usefixtures('driver')
class TestBase:

    def test_search_for_element(self):
        self.driver.find_element_by_id('search').click()
        self.driver.find_element_by_id('search').send_keys("'t Hoeksken")
        self.driver.find_element_by_id('cityName').click()
        map = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout[2]')
        assert map.is_displayed()


    def test_element_on_the_map(self):
        self.driver.find_element_by_id('search').click()
        self.driver.find_element_by_id('search').send_keys("'t Hoeksken")
        self.driver.find_element_by_id('cityName').click()
        element = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout[2]/android.widget.ImageView')
        assert element.is_displayed()

    def test_screen_scroll(self):
        touch = TouchAction(self.driver)
        touch.press(x=535, y=2022).move_to(x=535, y=56).release().perform()
        for x in range(5):
            touch = TouchAction(self.driver)
            touch.press(x=535, y=2022).move_to(x=535, y=56).release().perform()
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[14]').click()










"""""""""""
    def test_scroll_until_found_element():
    
        # function search for element until is found
        # scroll until element is found 
"""""""""