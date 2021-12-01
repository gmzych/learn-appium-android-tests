from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from support_funcs import BasePage

class MainPage(BasePage):

# Xpaths
    search_button = (MobileBy.ID,'search')
    map_element = (MobileBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout[2]')
    city_name = (MobileBy.ID,'cityName')
    main_page = (MobileBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.RelativeLayout')
    icon_on_the_map = (MobileBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout[2]/android.widget.ImageView')
    main_page_title = (MobileBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.TextView')
# Actions

# akcja znalezienie searcha
    def get_search_engine(self):
        return self.wait_for_visibility_of_element(self.search_button).click()
# akcja znalezienie mapy
    def map_get_result(self):
        return self.wait_for_visibility_of_element(self.map_element)

# akcja zlokalizuj icone 'Google' na mapie
    def map_check_if_icon_isdisplayed(self):
        return self.wait_for_visibility_of_element(self.icon_on_the_map)

# akcja zlokalizuj tytuł na stronie głównej
    def check_if_title_is_displayed(self,title_value):
        title = self.wait_for_visibility_of_element(self.main_page_title)
        title.text == title_value
        return title

# akcja sprawdzenie poprawnosci wyświetlenia strony głownej
    def main_page_is_displayed(self):
        return self.wait_for_visibility_of_element(self.main_page)

# akcja powrot do strony głownej
    def get_back_to_main_page(self):
        return self.driver.back()

# akcja wyczyszczenie searcha
    def get_clean_search_engine(self):
        return self.wait_for_visibility_of_element(self.search_button).clear()

# akcja wpisanie dowolnego miasta do searcha
    def search_get_display_result(self,search_value):
        elem = self.wait_for_visibility_of_element(self.search_button)
        elem.send_keys(search_value)
        return elem

# akcja kliknięcia wybranego miasta na liscie
    def search_get_result_click(self,result_elem):
        elem = self.driver.find_element_by_xpath(result_elem).click()
        return elem

# akcja scroll do wybranego miejsca
    def scroll_to_specific_element(self,scroll_to_value):
        elem = self.driver.find_element_by_android_uiautomator(f'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("{scroll_to_value}").instance(0));')
        self.driver.implicitly_wait(30)
        return elem




""""
       
    def screen_scroll2(self):
        touch = TouchAction(self.driver)
        touch.press(x=535, y=2022).move_to(x=535, y=56).release().perform()
        for x in range(5):
                touch = TouchAction(self.driver)
                touch.press(x=535, y=2022).move_to(x=535, y=56).release().perform()
        city_name = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[13]/android.widget.TextView')
        assert city_name.is_displayed()

"""""