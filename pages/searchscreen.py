from pages.base import BasePage


class Search(BasePage):

    _navigation_buttons_btn_show_on_map = 'show_on_map'

    # verify that the elements are displayed
    def check_is_displayed_show_on_map_button(self):
        super().is_displayed_by_id(self._navigation_buttons_btn_show_on_map)

    def check_is_displayed_categories_button(self):
        super().is_displayed_by_name('Categories')

    # click on the element
    def click_on_categories_button(self):
        super().click_by_name('Categories')

    def click_on_food_button(self):
        super().click_by_name('Food')
