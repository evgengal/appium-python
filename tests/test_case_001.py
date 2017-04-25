# -*- coding: utf-8 -*-"
import unittest
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
        homepage = Home(self.driver)
        searchpage = Search(self.driver)
        objectinfoscreen = ObjectInfo(self.driver)
        editplace = EditPlace(self.driver)

        demo_data_001 = {
            "latin_name": "Rukkola Latin",
            "zipcode": "109012",
            "email": "test@test.com",
            "opening_time": "9:30",
            "closing_time": "21:15",
            "cuisine": "Austrian",
            "new_opening_hours": ""
        }

        # Disable show offers
        homepage.click_on_menu_button()
        homepage.click_on_settings_button()
        self.driver.implicitly_wait(3)
        homepage.click_on_other_settings()
        homepage.switch_show_offers()
        homepage.go_back()
        homepage.go_back()

        # Check my_position button is displayed
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
        searchpage.check_is_displayed_categories_button()
        searchpage.click_on_categories_button()
        # Tap Food button
        searchpage.click_on_food_button()
        # Check results
        self.driver.implicitly_wait(10)
        searchpage.check_is_displayed_show_on_map_button()
        # Choose Ruccola Restaurant
        searchpage.check_is_displayed_object_with_name('Руккола')
        searchpage.click_by_name('Руккола')
        # Check results
        homepage.check_is_displayed_map_surfaceview()
        homepage.check_is_displayed_place_preview()

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
        editplace.click_by_name_strong('Latin')
        editplace.click_by_name('Руккола')

        editplace.check_is_displayed_btn_add_langs()
        editplace.check_is_displayed_object_with_name('Latin')
        editplace.input_new_lang("Rukkola Latin")
        # start work around, need to add function: clear focus on touch outside
        editplace.click_on_btn_add_langs()
        editplace.tap_back_in_toolbar()
        # end work around
        # Add zipcode
        editplace.scroll_to_block_opening_hours()
        editplace.input_new_zipcode(demo_data_001["zipcode"])
        editplace.click_on_opening_hours()
        # Add new opening hours
        editplace.click_on_time_open()
        editplace.set_new_time(demo_data_001["opening_time"])
        editplace.set_new_time(demo_data_001["closing_time"])
        editplace.click_on_btn_save()
        editplace.scroll_to_block_opening_hours()
        same_value = self.driver.find_element_by_id('opening_hours')
        demo_data_001["new_opening_hours"] = same_value.text
        # Add new email
        editplace.scroll_to_block_cuisine()
        editplace.input_new_email(demo_data_001["email"])
        # Add new cuisine
        editplace.click_on_cuisine()
        editplace.click_by_name(demo_data_001["cuisine"])
        editplace.click_on_btn_save()
        # Turn on wifi
        editplace.scroll_to_block_wifi()
        editplace.click_on_sw_wifi()
        # Save new values
        editplace.click_on_btn_save()
        editplace.skip_dialog_send_it_to_all_users()
        editplace.check_is_displayed_alert_register()
        editplace.check_is_displayed_alert_login_osm()
        editplace.tap_outside_to_disable_dialog()
        # Check new values
        objectinfoscreen.check_tv_title_is('Руккола')
        email = demo_data_001["new_opening_hours"]
        cuisine = demo_data_001["cuisine"]
        new_opening_hours = demo_data_001["new_opening_hours"]
        objectinfoscreen.is_displayed_by_name(new_opening_hours)
        objectinfoscreen.is_displayed_by_name(email)
        objectinfoscreen.check_one_of_cuisine_is_displayed(cuisine)
        objectinfoscreen.check_is_displayed_tv_place_wifi()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MapsMeAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
