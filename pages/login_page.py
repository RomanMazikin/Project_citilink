from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import  allure
from base.base_class import Base
from utilities.logger import Logger


class LoginPage(Base):

    # Locators
    account_button = '//div[@class="css-1wyvf5z eyoh4ac0"]'
    user_email = '//input[@name="login"]'
    user_password = '//input[@name="pass"]'
    button_enter = '//button[@class="e4uhfkv0 css-1yh1imp e4mggex0"]'

    # Getters
    def get_account_button(self):
        return WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.account_button)))

    def get_user_email(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.user_email)))

    def get_user_password(self):
        return WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.user_password)))

    def get_button_enter(self):
        return WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.button_enter)))

    # Actions
    def click_account_button(self):
        self.get_account_button().click()
        print("click account button")

    def input_user_email(self, email):
        self.get_user_email().send_keys(email)
        print("input email")

    def input_password(self, password):
        self.get_user_password().send_keys(password)
        print("input password")

    def click_button_enter(self):
        self.get_button_enter().click()
        print("click button enter")

    # Methods

    def authorisation(self):
        with allure.step("authorisation"):
            Logger.add_start_step(method="authorisation")
            self.driver.get("https://www.citilink.ru/")
            self.driver.maximize_window()
            self.click_account_button()
            self.input_user_email("testqa2606@rambler.ru")
            self.input_password("Qa26062023")
            self.click_button_enter()
            Logger.add_end_step(url=self.driver.current_url, method="authorisation")

