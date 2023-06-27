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
    name_product = '//a[@href="/product/smartfon-xiaomi-poco-x5-pro-5g-128gb-6gb-chernyi-3g-4g-2sim-6-67-amole-1901551/"]'
    price_product = '(//span[@data-meta-price="27990"])[1]'



    # Getters
    def get_page_word(self):
        return WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.page_word)))

    def get_button_checkout(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.button_checkout)))

    def get_name_product(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.name_product)))

    def get_price_product(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.price_product)))

    # Actions
    def value_page_word(self):
        word = self.get_page_word().text
        print("get value page word")
        return word

    def click_button_checkout(self):
        self.get_button_checkout().click()
        print("click button checkout")

    def value_name_product(self):
        name = self.get_name_product().text
        print("value name product")
        return name

    def value_price_product(self):
        price = self.get_price_product().text
        print("value name product")
        return price

    # Methods

    def checkout(self):
        self.assert_value("Корзина", self.value_page_word())
        self.click_button_checkout()

