import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from pages.cart_page import CartPage


class OrderInfo(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    fist_name = '//input[@name="contact-form_firstName"]'
    last_name = '//input[@name="contact-form_lastName"]'
    button_submit_order = '//button[@data-meta-name="SubmitButton"]'
    # final_name_product = '[data-meta-id="91f80d76-c863-49f9-8ba9-13ed51c0ba1f"] [class="e27li280 e106ikdt0 css-1qo2d1j e1gjr6xo0"]'
    # final_price = '(//span[@data-meta-price="27990"])[3]'

    # Getters

    def get_fist_name(self):
        return WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.fist_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_button_submit_order(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.button_submit_order)))

    # def get_final_name_product(self):
    #     return WebDriverWait(self.driver, 20).until(
    #         EC.element_to_be_clickable((By.CSS_SELECTOR, self.final_name_product)))
    #
    # def get_final_price(self):
    #     return WebDriverWait(self.driver, 20).until(
    #         EC.element_to_be_clickable((By.XPATH, self.final_price)))

    # Actions
    def clear_fist_name(self):
        self.get_fist_name().clear()
        print("clear first name")

    def clear_last_name(self):
        self.get_last_name().clear()
        print("clear last name")

    def input_fist_name(self):
        self.get_fist_name().send_keys("Ivan")
        print("input first name")

    def input_last_name(self):
        self.get_last_name().send_keys("Ivanov")
        print("input last name")

    def click_button_submit_order(self):
        self.get_button_submit_order().click()
        print("Thank you for your order")

    # def value_final_name_product(self):
    #     name1 = self.get_final_name_product().text
    #     print("value name product")
    #     return name1
    #
    # def value_final_price(self):
    #     price1 = self.get_final_price().text
    #     print("value name product")
    #     return price1

    # Methods

    def confirmation_order(self):
        self.clear_fist_name()
        self.clear_last_name()
        self.input_fist_name()
        self.input_last_name()
        self.scroll_to(self.get_button_submit_order())
        # self.click_button_submit_order()  закомментировал чтобы не оформился заказ
        time.sleep(1)


