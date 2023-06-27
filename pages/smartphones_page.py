import time

from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class SmartphonesPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    checkbox_xiaomi = '//input[@id="xiaomi"]'
    checkbox_128gb = '//input[@id="23178_214128d1gb"]'
    filter_battery = '//div[@data-meta-value="Емкость батареи"]'
    checkbox_filter_battery_5000 = '//input[@id = "19462_214"]'
    button_add_to_cart = '[data-meta-product-id="1901551"] [class="e1kkg8nh0 app-catalog-1e6t8kn e4mggex0"]'
    button_go_to_cart = '//button[@class="e4uhfkv0 css-10je9jt e4mggex0"]'
    button_cookie = '//button[@class="e4uhfkv0 css-1jfe691 e4mggex0"]'

    # Getters
    def get_button_cookie(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.button_cookie)))

    def get_checkbox_xiaomi(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.checkbox_xiaomi)))

    def get_checkbox_128gb(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.checkbox_128gb)))

    def get_filter_battery(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_battery)))

    def get_checkbox_filter_battery_5000(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.checkbox_filter_battery_5000)))

    def get_button_add_to_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.button_add_to_cart)))

    def get_button_go_to_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_go_to_cart)))

    # Actions
    def click_button_cookie(self):
        self.get_button_cookie().click()
        print("click button cookie")

    def click_checkbox_xiaomi(self):
        self.get_checkbox_xiaomi().click()
        print("click checkbox xiaomi")

    def click_checkbox_128gb(self):
        self.get_checkbox_128gb().click()
        print("click checkbox 128gb")

    def click_filter_battery(self):
        self.get_filter_battery().click()
        print("click filter battery")

    def click_checkbox_filter_battery_5000(self):
        self.get_checkbox_filter_battery_5000().click()
        print("click checkbox battery 5000")
        time.sleep(1)

    def click_button_add_to_cart(self):
        self.get_button_add_to_cart().click()
        print("click button add to cart")

    def click_button_go_to_cart(self):
        self.get_button_go_to_cart().click()
        print("click button go to cart")

    # Methods

    def select_poco_x5pro(self):
        self.click_button_cookie()
        self.scroll_to(self.get_checkbox_xiaomi())
        self.click_checkbox_xiaomi()
        self.scroll_to(self.get_checkbox_128gb())
        self.click_checkbox_128gb()
        self.scroll_to(self.get_filter_battery())
        self.click_filter_battery()
        self.click_checkbox_filter_battery_5000()
        self.scroll_to(self.get_button_add_to_cart())
        self.click_button_add_to_cart()
        try:
            self.click_button_go_to_cart()
        except TimeoutException:
            pass

