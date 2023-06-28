from selenium import webdriver
from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_info_page import OrderInfo
from pages.smartphones_page import SmartphonesPage


def test_buy_product(set_group):

    driver = webdriver.Chrome()

    login = LoginPage(driver)
    login.authorisation()

    mp = MainPage(driver)
    mp.select_category_smartphones()

    sp = SmartphonesPage(driver)
    sp.select_poco_x5pro()

    cp = CartPage(driver)
    cp.checkout()

    oi = OrderInfo(driver)
    oi.confirmation_order()

    



