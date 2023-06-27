import time

from selenium.webdriver import ActionChains


class Base:
    def __init__(self, driver):
        self.driver = driver

    def scroll_to(self, path):
        action = ActionChains(self.driver)
        action.move_to_element(path).perform()

    def assert_value(self, value1, value2):
        assert value1 == value2
        print("right value")
