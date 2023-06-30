import time
import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from utilities.logger import Logger


class MainPage(Base):

    # Locators
    catalog_menu = '//a[@data-meta-name="DesktopHeaderFixed__catalog-menu"]'
    category_smartphones = '//a[@data-meta-name="DesktopMenu__sub-category"]'

    # Getters
    def get_catalog_menu(self):
        return WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.catalog_menu)))

    def get_category_smartphones(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.category_smartphones)))

    # Actions
    def click_catalog_menu(self):
        self.get_catalog_menu().click()
        print("click catalog menu")
        time.sleep(1)

    def click_category_smartphones(self):
        self.get_category_smartphones().click()
        print("click category smartphones")

    # Methods

    def select_category_smartphones(self):
        with allure.step("select_category_smartphones"):
            Logger.add_start_step(method="select_category_smartphones")
            self.click_catalog_menu()
            self.click_category_smartphones()
            Logger.add_end_step(url=self.driver.current_url, method="select_category_smartphones")
