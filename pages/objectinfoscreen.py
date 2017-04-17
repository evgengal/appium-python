import unittest
from pages.base import BasePage


class ObjectInfo(BasePage, unittest.TestCase):

    _tv_title = 'tv__title'
    _tv_subtitle = 'tv__subtitle'
    _tv_address = 'tv__address'
    _av_direction = 'av__direction'
    _tv_straight_distance = 'tv__straight_distance'
    _today_opening_hours = 'today_opening_hours'
    _tv_place_phone = 'tv__place_phone'
    _tv_place_website = 'tv__place_website'
    _tv_place_cuisine = 'tv__place_cuisine'
    _tv_place_wifi = 'tv__place_wifi'
    _btn_edit_place = 'tv__editor'
    time_from_objectinfo = ''
    phone_from_objectinfo = ''
    website_from_objectinfo = ''
    cuisine_from_objectinfo = ''

    # verify that the elements are displayed
    def check_is_displayed_av_direction(self):
        super().is_displayed_by_id(self._av_direction)

    def check_is_displayed_tv_straight_distance(self):
        super().is_displayed_by_id(self._tv_straight_distance)

    def check_is_displayed_today_opening_hours(self):
        super().is_displayed_by_id(self._today_opening_hours)
        time_from_objectinfo = self.driver.find_element_by_id('today_opening_hours')

    def check_is_displayed_tv_place_phone(self):
        super().is_displayed_by_id(self._tv_place_phone)
        phone_from_objectinfo = self.driver.find_element_by_id('tv__place_phone')

    def check_is_displayed_tv_place_website(self):
        super().is_displayed_by_id(self._tv_place_website)
        website_from_objectinfo = self.driver.find_element_by_id('tv__place_website')

    def check_is_displayed_tv_place_cuisine(self):
        super().is_displayed_by_id(self._tv_place_cuisine)
        cuisine_from_objectinfo = self.driver.find_element_by_id('tv__place_cuisine')

    def check_one_of_cuisine_is_displayed(self, value):
        super().is_displayed_by_id(self._tv_place_cuisine)
        fulltext = self.driver.find_element_by_id('tv__place_cuisine').text
        self.assertTrue(value in fulltext)

    def check_is_displayed_tv_place_wifi(self):
        super().is_displayed_by_id(self._tv_place_wifi)

    def check_is_displayed_tv_editor(self):
        super().is_displayed_by_id(self._btn_edit_place)

    # check the content of the element
    def check_tv_title_is(self, value):
        my_tv_title = self.driver.find_element_by_id('tv__title')
        self.assertTrue(my_tv_title, value)

    def check_tv_subtitle_is(self, value):
        my_tv_subtitle = self.driver.find_element_by_id('tv__subtitle')
        self.assertTrue(my_tv_subtitle, value)

    def check_tv_address_is(self, value):
        my_tv_address = self.driver.find_element_by_id('tv__address')
        self.assertTrue(my_tv_address, value)

    # click on the element
    def click_on_btn_edit_place(self):
        super().click_by_id(self._btn_edit_place)
