import time

import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from pages.cart_page import CartPage
from utilities.logger import Logger


class OrderInfo(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    fist_name = '//input[@name="contact-form_firstName"]'
    last_name = '//input[@name="contact-form_lastName"]'
    button_submit_order = '//button[@data-meta-name="SubmitButton"]'

    # Getters

    def get_fist_name(self):
        return WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.fist_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_button_submit_order(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.button_submit_order)))

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

    # Methods

    def confirmation_order(self):
        with allure.step("confirmation_order"):
            Logger.add_start_step(method="confirmation_order")
            self.clear_fist_name()
            self.clear_last_name()
            self.input_fist_name()
            self.input_last_name()
            self.scroll_to(self.get_button_submit_order())
            # self.click_button_submit_order()  закомментировал чтобы не оформился заказ
            Logger.add_end_step(url=self.driver.current_url, method="confirmation_order")
            time.sleep(1)


