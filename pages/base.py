from appium.webdriver.common.touch_action import TouchAction
from datetime import datetime


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def click_by_id(self, element_id):
        self.driver.find_element_by_id(element_id).click()

    def click_by_name(self, name):
        self.driver.find_element_by_name(name).click()

    def click_on_object_with_name(self, value):
        self.click_by_name(value)

    def input_text_by_id(self, element_id, value):
        self.driver.find_element_by_id(element_id).send_keys(value)

    def input_text_by_name(self, name, value):
        self.driver.find_element_by_name(name).send_keys(value)

    def is_displayed_by_id(self, element_id):
        self.driver.find_element_by_id(element_id).is_displayed()

    def is_displayed_by_name(self, name):
        self.driver.find_element_by_name(name).is_displayed()

    def check_is_displayed_object_with_name(self, value):
        self.is_displayed_by_name(value)

    def find_and_tap_arrow_in_center_of_view(self):
        dimensions = self.driver.get_window_size()
        screen_width = dimensions["width"] / 2
        screen_height = dimensions["height"] / 2
        self.single_tap(screen_width, screen_height)

    def tap_outside_to_disable_dialog(self):
        dimensions = self.driver.get_window_size()
        screen_width = dimensions["width"] / 2
        screen_height = "80.0"
        self.single_tap(screen_width, screen_height)

    def single_tap(self, x, y):
        action = TouchAction(self.driver)
        action.tap(None, x, y).perform()

    def scroll_to_element_with_id(self, element_id):
        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector()'
            '.scrollable(true).instance(0)).scrollIntoView('
            'new UiSelector().resourceId(\"com.mapswithme.maps.pro:id/' + element_id + '\").instance(0));')

    def scroll_to_element_with_text(self, text):
        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector()'
            '.scrollable(true).instance(0)).scrollIntoView('
            'new UiSelector().text(\"' + text + '\").instance(0));')

    def get_text_from_edittext_with_parent_element(self, text):
        child_text = self.driver.find_element_by_android_uiautomator(
            'new UiSelector().text(\"' + text + '\")'
            '.childSelector(new UiSelector().className(android.widget.EditText).clickable(true))')
        return child_text

    def get_text_from_textview_with_parent_element(self, text):
        child_text = self.driver.find_element_by_android_uiautomator(
            'new UiSelector().text(\"' + text + '\")'
            '.childSelector(new UiSelector().className(android.widget.TextView))')
        return child_text

    def tap_back_in_toolbar(self):
        back_button = self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId(\"com.mapswithme.maps.pro:id/toolbar\")'
            '.childSelector(new UiSelector().className(android.widget.ImageButton))')
        back_button.click()

    def set_new_time(self, time_24):
        time_format_24 = datetime.strptime(time_24, "%H:%M")
        time_hour = time_format_24.strftime("X%I").replace('X0', 'X').replace('X', '')
        time_min = time_format_24.strftime("%M")
        time_format = time_format_24.strftime("%p")
        self.click_by_name(time_hour)
        self.click_by_name(time_min)
        self.click_by_name(time_format)
        self.click_by_id("button1")

    def set_time_unit(self):
        time = self.driver.find_element_by_android_uiautomator(
            'new UiSelector().new UiSelector().className(android.widget.RadialTimePickerView$RadialPickerTouchHelper)')
        time.send_keys("10")

    def hide_keyboard(self):
        self.driver.hide_keyboard()

    def go_back(self):
        self.driver.back()

    def tap_navigate_next(self):
        self.driver.press_keycode(66)
