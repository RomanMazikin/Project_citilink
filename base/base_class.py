import time

from selenium.webdriver import ActionChains


class Base:
    def __init__(self, driver):
        self.driver = driver

    def scroll_to(self, path):
        action = ActionChains(self.driver)
        action.move_to_element(path).perform()

    def assert_page_word(self, page_word, fact_word):
        assert page_word == fact_word
        print("right page word")
