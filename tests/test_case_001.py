# -*- coding: utf-8 -*-"
import unittest
import time
from pages.homescreen import Home
from pages.searchscreen import Search
from pages.objectinfoscreen import ObjectInfo
from pages.editplacescreen import EditPlace
from general.driver import driver


class MapsMeAndroidTests(unittest.TestCase):
    def setUp(self):
        self.driver = driver
        self.driver.wait_activity('appActivity', 10, 1)

    def tearDown(self):
        # end the session
        self.driver.quit()

    def test_case_001(self):

        demo_data_001 = {
            "latin_name": "Rukkola Latin",
            "zipcode": "109012",
            "email": "test@test.com",
        }

        # Check my_position button is displayed
        homepage = Home(self.driver)
        homepage.check_is_displayed_my_position_button()
        # Tap my_position button
        homepage.click_on_my_position_button()
        # Tap on the arrow in the center of the screen
        homepage.find_and_tap_arrow_in_center_of_view()
        # Check that my location was found and save my gps and tap back
        homepage.check_is_displayed_place_preview()
        homepage.click_on_place_preview()
        homepage.save_my_coordinates()
        # Hide pp__preview
        homepage.go_back()
        # Check search button is displayed
        homepage.check_is_displayed_search_button()
        # Tap search button
        homepage.click_on_search_button()
        # Tap Categories button
        searchpage = Search(self.driver)
        searchpage.click_on_categories_button()
        # Tap Food button
        searchpage.click_on_food_button()
        # Check results
        self.driver.implicitly_wait(10)
        searchpage.check_is_displayed_show_on_map_button()
        # Choose Ruccola Restaurant
        searchpage.check_is_displayed_object_with_name('Руккола')
        searchpage.click_on_object_with_name('Руккола')
        # Check results
        homepage.check_is_displayed_map_surfaceview()
        homepage.check_is_displayed_place_preview()
        objectinfoscreen = ObjectInfo(self.driver)
        objectinfoscreen.check_tv_title_is('Руккола')
        objectinfoscreen.check_tv_subtitle_is('Restaurant • Italian')
        objectinfoscreen.check_tv_address_is('Никольская улица, 8/1 с1')
        objectinfoscreen.check_is_displayed_av_direction()
        objectinfoscreen.check_is_displayed_tv_straight_distance()
        # Open full info
        homepage.click_on_place_preview()
        # Check full info
        objectinfoscreen.check_is_displayed_today_opening_hours()
        objectinfoscreen.check_is_displayed_tv_place_phone()
        objectinfoscreen.check_is_displayed_tv_place_website()
        homepage.check_format_coordinates()
        objectinfoscreen.check_is_displayed_tv_place_cuisine()
        objectinfoscreen.check_is_displayed_tv_editor()
        # Open edit place screen and check
        objectinfoscreen.click_on_btn_edit_place()
        editplace = EditPlace(self.driver)
        editplace.scroll_to_block_opening_hours()
        editplace.check_opening_hours_value()
        editplace.check_phone_value()
        editplace.check_website_value()
        editplace.scroll_to_block_cuisine()
        editplace.check_cuisine_value()
        # Add latin language
        editplace.scroll_to_btn_add_langs()
        editplace.click_on_btn_add_langs()
        editplace.scroll_to_latin_lang()
        editplace.click_on_object_with_name('Latin')
        editplace.check_is_displayed__btn_add_langs()
        editplace.check_is_displayed_object_with_name('Latin')
        editplace.input_new_lang(demo_data_001["latin_name"])
        # start work around, need to add function: clear focus on touch outside
        editplace.click_on_btn_add_langs()
        editplace.tap_back_in_toolbar()
        # end work around
        # Add zipcode
        editplace.scroll_to_block_opening_hours()
        editplace.input_new_zipcode(demo_data_001["zipcode"])
        #editplace.check_is_displayed_object_with_name(demo_data_001["zipcode"])
        editplace.click_on_opening_hours()
        editplace.click_on_time_open()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MapsMeAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
