import unittest
from pages.base import BasePage
from pages.objectinfoscreen import ObjectInfo


class EditPlace(BasePage, unittest.TestCase):

    _toolbar = 'toolbar'
    _category = 'category'
    _block_opening_hours = 'block_opening_hours'
    _opening_hours = 'opening_hours'
    _block_cuisine = 'block_cuisine'
    _block_zipcode = 'block_zipcode'
    _cuisine = 'cuisine'
    _btn_add_langs = 'add_langs'
    _time_open = 'time_open'

    # verify that the elements are displayed
    def check_is_displayed_id_category(self):
        super().is_displayed_by_id(self._category)

    def check_is_displayed__btn_add_langs(self):
        super().is_displayed_by_id(self._btn_add_langs)

    # scroll to element
    def scroll_to_block_opening_hours(self):
        super().scroll_to_element_with_id(self._block_opening_hours)

    def scroll_to_btn_add_langs(self):
        super().scroll_to_element_with_id(self._btn_add_langs)

    def scroll_to_block_cuisine(self):
        super().scroll_to_element_with_id(self._block_cuisine)

    def scroll_to_block_zipcode(self):
        super().scroll_to_element_with_id(self._block_zipcode)

    def scroll_to_latin_lang(self):
        super().scroll_to_element_with_text("Latin")

    # click on the element
    def click_on_toolbar_for_disable_focus(self):
        super().click_by_id(self._toolbar)

    def click_on_btn_add_langs(self):
        super().click_by_id(self._btn_add_langs)

    def click_on_opening_hours(self):
        super().click_by_id(self._opening_hours)

    def click_on_time_open(self):
        super().click_by_id(self._time_open)

    # input values
    def input_new_lang(self, value):
        super().input_text_by_name('Latin', value)
        self.go_back()

    def input_new_zipcode(self, value):
        super().input_text_by_name('ZIP Code', value)
        self.go_back()

    # check info
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
