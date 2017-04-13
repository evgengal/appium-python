from appium.webdriver.common.touch_action import TouchAction


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def click_by_id(self, element_id):
        self.driver.find_element_by_id(element_id).click()

    def click_by_name(self, name):
        self.driver.find_element_by_name(name).click()

    def is_displayed_by_id(self, element_id):
        self.driver.find_element_by_id(element_id).is_displayed()

    def is_displayed_by_name(self, name):
        self.driver.find_element_by_name(name).is_displayed()

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

