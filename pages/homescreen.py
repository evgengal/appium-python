import unittest
from pages.base import BasePage


class Home(BasePage, unittest.TestCase):

    _navigation_buttons_btn_my_position = 'my_position'
    _map_surfaceview = 'map_surfaceview'
    _place_preview = 'pp__preview'
    _place_coordinates = 'tv__place_latlon'
    _menu_frame_btn_search = 'search'
    _menu_frame_btn_menu = 'menu'
    _content_frame_btn_settings = 'settings'
    coordinates_in_decimal_degrees1 = ''

    def scroll_to_latin_lang(self):
        super().scroll_to_element_with_text("Руккола")

    # verify that the elements are displayed
    def check_is_displayed_my_position_button(self):
        super().is_displayed_by_id(self._navigation_buttons_btn_my_position)

    def check_is_displayed_map_surfaceview(self):
        super().is_displayed_by_id(self._map_surfaceview)

    def check_is_displayed_place_preview(self):
        super().is_displayed_by_id(self._place_preview)

    def check_is_displayed_search_button(self):
        super().is_displayed_by_id(self._menu_frame_btn_search)

    # click on the element
    def click_on_my_position_button(self):
        super().click_by_id(self._navigation_buttons_btn_my_position)

    def click_on_place_preview(self):
        super().click_by_id(self._place_preview)

    def click_on_search_button(self):
        super().click_by_id(self._menu_frame_btn_search)

    def click_on_menu_button(self):
        super().click_by_id(self._menu_frame_btn_menu)

    def click_on_settings_button(self):
        super().click_by_id(self._content_frame_btn_settings)

    def click_on_place_coordinates(self):
        super().click_by_id(self._place_coordinates)

    def click_on_other_settings(self):
        super().click_by_name('Miscellaneous')

    def switch_show_offers(self):
        super().click_by_name('Show offers')

    def save_my_coordinates(self):
        my_coordinates = self.driver.find_element_by_id('tv__place_latlon')
        print("My coordinates is : ", my_coordinates.text)

    def check_format_coordinates(self):
        coordinates_in_decimal_degrees1 = self.driver.find_element_by_id('tv__place_latlon')
        print("Coordinates in decimal degrees : ", coordinates_in_decimal_degrees1.text)
        homepage = Home(self.driver)
        homepage.click_on_place_coordinates()
        coordinates_in_degrees_and_minutes1 = self.driver.find_element_by_id('tv__place_latlon')
        homepage.click_on_place_coordinates()
        coordinates_in_decimal_degrees2 = self.driver.find_element_by_id('tv__place_latlon')
        self.assertTrue(coordinates_in_decimal_degrees1, coordinates_in_decimal_degrees2)
        coordinates_in_degrees_and_minutes2 = self.driver.find_element_by_id('tv__place_latlon')
        homepage.click_on_place_coordinates()
        self.assertTrue(coordinates_in_degrees_and_minutes1, coordinates_in_degrees_and_minutes2)
        print("Coordinates in degrees and minutes : ", coordinates_in_degrees_and_minutes1.text)
        homepage.click_on_place_coordinates()
