from .pages.basket_page import BasketPage
from .pages.base_page import BasePage
from .pages.login_page import LoginPage
from .pages.product_page import AddProduct
import pytest
import time

@pytest.mark.login_guest
class TestLoginFromMainPage():
    # не забываем передать первым аргументом self
    def test_guest_can_go_to_login_page(self, browser):
        # реализация теста
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = AddProduct(browser, link)
        page.open()
        page.guest_can_go_to_login_page_from_product_page()

    def test_guest_should_see_login_link(self, browser):
        # реализация теста
        link = "http://selenium1py.pythonanywhere.com/"
        page = LoginPage(browser, link)
        page.open()
        page.should_be_login_link()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasketPage(browser, link)
    page.open()
    page.guest_cant_see_product_in_basket_opened_from_main_page()
