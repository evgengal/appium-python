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

    def check_is_displayed_av_direction(self):
        super().is_displayed_by_id(self._av_direction)

    def check_is_displayed_tv_straight_distance(self):
        super().is_displayed_by_id(self._tv_straight_distance)

    def check_is_displayed_today_opening_hours(self):
        super().is_displayed_by_id(self._today_opening_hours)

    def check_is_displayed_tv_place_phone(self):
        super().is_displayed_by_id(self._tv_place_phone)

    def check_is_displayed_tv_place_website(self):
        super().is_displayed_by_id(self._tv_place_website)

    def check_tv_title_is(self, value):
        my_tv_title = self.driver.find_element_by_id('tv__title')
        self.assertTrue(my_tv_title, value)

    def check_tv_subtitle_is(self, value):
        my_tv_subtitle = self.driver.find_element_by_id('tv__subtitle')
        self.assertTrue(my_tv_subtitle, value)

    def check_tv_address_is(self, value):
        my_tv_address = self.driver.find_element_by_id('tv__address')
        self.assertTrue(my_tv_address, value)
