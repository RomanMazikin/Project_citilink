import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class CartPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    page_word = '//span[@class="e1ys5m360 e106ikdt0 css-1f8xctp e1gjr6xo0"]'
    button_checkout = '//button[@title="Перейти к оформлению"]'

    # Getters
    def get_page_word(self):
        return WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.page_word)))

    def get_button_checkout(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.button_checkout)))

    # Actions
    def value_page_word(self):
        word = self.get_page_word().text
        print("get value page word")
        return word

    def click_button_checkout(self):
        self.get_button_checkout().click()
        print("click button checkout")

    # Methods

    def checkout(self):
        self.assert_page_word("Корзина", self.value_page_word())
        self.click_button_checkout()
