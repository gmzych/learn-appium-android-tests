import pytest


@pytest.mark.usefixtures('driver')
class TestObjects:

# test sprawdza czy mapa została wyświetlona po przejsciu z miasta z listy
    def test_map_get_result(self):
        self.main_page.get_search_engine()
        self.main_page.find_element_and_go_back()
        map_element = self.main_page.map_get_result()
        assert map_element.is_displayed()
# test sprawdza wejscie na mape i powrot na stronę główna
    def test_find_element_and_go_back(self):
        self.main_page.get_search_engine()
        self.main_page.search_get_display_result('A da Beja')
        self.main_page.search_get_result_click('/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout/android.widget.TextView')
        self.main_page.get_back_to_main_page()
        self.main_page.get_clean_search_engine()
        main_page = self.main_page.main_page_is_displayed()
        assert main_page.is_displayed()
# test scrolluj do wybranego tekstu, wybierz i sprawdz czy wyświetliła sie mapa
    def test_scroll_to_specific_element(self):
        self.main_page.scroll_to_specific_element("Aast, FR")
        self.main_page.search_get_result_click('/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[14]/android.widget.TextView')
        map = self.main_page.map_get_result()
        assert map.is_displayed()
# test scrolluj do wybranego tekstu, wybierz i sprawdz czy na mapie wyświetliła się ikona google
    def test_check_if_icon_on_the_map_is_displayed(self):
        self.main_page.scroll_to_specific_element('Abetone, IT')
        self.main_page.search_get_result_click('/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[19]/android.widget.TextView')
        icon_on_the_map = self.main_page.map_check_if_icon_isdisplayed()
        assert icon_on_the_map.is_displayed()
# test sprawdzający poprawność wyświetlanego tytułu na stronie głownej
    def test_check_if_title_is_displayed(self):
        title = self.main_page.check_if_title_is_displayed('Mobile Assignment')
        assert title.is_displayed()
# test scrolluj do wybranego tekstu i wybierz miasto nastepnie cofnij,powtorz czynnosc
    def test_scoll_to_specific_element_and_go_back(self):
        self.main_page.scroll_to_specific_element('Abanilla, ES')
        self.main_page.search_get_result_click('/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[14]/android.widget.TextView')
        self.main_page.get_back_to_main_page()
        self.main_page.scroll_to_specific_element('Abatskoye, RU')
        self.main_page.search_get_result_click('/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[18]/android.widget.TextView')
        self.main_page.get_back_to_main_page()
        assert self.main_page.main_page_is_displayed()



