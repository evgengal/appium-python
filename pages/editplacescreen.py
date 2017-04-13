import unittest
from pages.base import BasePage
from pages.objectinfoscreen import ObjectInfo


class EditPlace(BasePage, unittest.TestCase):

    _category = 'category'
    _block_opening_hours = 'block_opening_hours'
    _opening_hours = 'opening_hours'
    _block_cuisine = 'block_cuisine'
    _cuisine = 'cuisine'

    # verify that the elements are displayed
    def check_is_displayed_id_category(self):
        super().is_displayed_by_id(self._category)

    def scroll_to_block_opening_hours(self):
        super().scroll_to_element_with_id(self._block_opening_hours)

    def scroll_to_block_cuisine(self):
        super().scroll_to_element_with_id(self._block_cuisine)

    def check_opening_hours_value(self):
        super().is_displayed_by_id(self._opening_hours)
        time_from_editscreen = self.driver.find_element_by_id('opening_hours')
        objectinfoscreen = ObjectInfo(self.driver)
        self.assertTrue(time_from_editscreen, objectinfoscreen.time_from_objectinfo)

    def check_phone_value(self):
        phone_from_editscreen = super().get_text_from_edittext_with_parent_element("Phone")
        objectinfoscreen = ObjectInfo(self.driver)
        self.assertTrue(phone_from_editscreen, objectinfoscreen.phone_from_objectinfo)

    def check_website_value(self):
        website_from_editscreen = super().get_text_from_edittext_with_parent_element("Website")
        objectinfoscreen = ObjectInfo(self.driver)
        self.assertTrue(website_from_editscreen, objectinfoscreen.website_from_objectinfo)

    def check_cuisine_value(self):
        cuisine_from_editscreen = self.driver.find_element_by_id('cuisine')
        objectinfoscreen = ObjectInfo(self.driver)
        self.assertTrue(cuisine_from_editscreen, objectinfoscreen.cuisine_from_objectinfo)
