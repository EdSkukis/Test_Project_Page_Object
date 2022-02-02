from .pages.basket_page import BasketPage
from .pages.base_page import BasePage
import time


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasketPage(browser, link)
    page.open()
    page.test_guest_cant_see_product_in_basket_opened_from_main_page()
