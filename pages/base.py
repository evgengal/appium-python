from appium.webdriver.common.touch_action import TouchAction


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def click_by_id(self, id):
        self.driver.find_element_by_id(id).click()

    def click_by_name(self, name):
        self.driver.find_element_by_name(name).click()

    def is_displayed_by_id(self, id):
        self.driver.find_element_by_id(id).is_displayed()

    def is_displayed_by_name(self, name):
        self.driver.find_element_by_name(name).is_displayed()

    def single_tap(self, x, y):
        action = TouchAction(self.driver)
        action.tap(None, x, y).perform()
