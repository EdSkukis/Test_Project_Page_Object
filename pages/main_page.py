from .base_page import BasePage
from .login_page import LoginPage
from .basket_page import BasketPage
from .product_page import AddProduct
from .locators import MainPageLocators
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
