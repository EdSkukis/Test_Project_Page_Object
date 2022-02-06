from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import AddProduct
import time # в начале файла
import pytest


@pytest.mark.need_review
class TestUserAddToBasketFromProductPage():
    #link = 'http://selenium1py.pythonanywhere.com/en-gb'

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        head_link = 'http://selenium1py.pythonanywhere.com/en-gb'
        # new user
        email = str(time.time()) + "@fakemail.org"
        password = '*AbCd_123_'

        link = head_link + '/accounts/login/'
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(email, password)
        page.should_be_user_is_login()
        #self.link = self.page
        # time.sleep(5)

    def test_user_cant_see_success_message(self, browser):
        # реализация теста

        link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
        page = AddProduct(browser, link)
        page.open()
        page.guest_cant_see_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        # реализация теста
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = AddProduct(browser, link)
        page.open()
        page.add_product_to_basket()

@pytest.mark.need_review
class TestGuestAddToBasketFromProductPage():
    def test_guest_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = AddProduct(browser, link)
        page.open()
        page.add_product_to_basket()

    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = BasketPage(browser, link)
        page.open()
        page.guest_cant_see_product_in_basket_opened_from_product_page()

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = AddProduct(browser, link)
        page.open()
        page.guest_can_go_to_login_page_from_product_page()




