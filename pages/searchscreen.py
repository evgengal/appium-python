from pages.base import BasePage


class Search(BasePage):

    _navigation_buttons_btn_show_on_map = 'show_on_map'

    def check_is_displayed_show_on_map_button(self):
        super().is_displayed_by_id(self._navigation_buttons_btn_show_on_map)

    def check_is_displayed_object_with_name(self, value):
        super().is_displayed_by_name(value)

    def click_on_categories_button(self):
        super().click_by_name('Categories')

    def click_on_food_button(self):
        super().click_by_name('Food')

    def click_on_object_with_name(self, value):
        super().click_by_name(value)