from selenium.common.exceptions import NoAlertPresentException  # в начале файла

from .base_page import BasePage
from .locators import AddProductPageLocators
from selenium.webdriver.common.by import By


class AddProduct(BasePage):
    def should_be_button_add_basket(self):
        assert self.browser.find_element(*AddProductPageLocators.BTN_ADD_TO_BASKET), "Add to basket button not presented"

    def should_be_name_of_product(self):
        assert self.browser.find_element(*AddProductPageLocators.PRODUCT_NAME), "Name of product don't found"

    def should_be_price_of_product(self):
        assert self.browser.find_element(*AddProductPageLocators.PRODUCT_PRICE), "Product Price not found"

    def should_be_msg_about_adding(self):
        # Проверка выхода сообщения что товар добавлен
        product_name = self.browser.find_element(*AddProductPageLocators.PRODUCT_NAME).text
        message = self.browser.find_element(*AddProductPageLocators.MESSAGE_ABOUT_ADDING).text

        assert product_name in message, "Product name not found on message"

    def compare_basket_and_product_price(self):
        # Сравнение цен товара и пустой корзины
        product_price = self.browser.find_element(*AddProductPageLocators.PRODUCT_PRICE).text
        basket_price = self.browser.find_element(*AddProductPageLocators.BASKET_PRICE).text

        assert product_price == basket_price, "Product price and basket price is not equal"


    def add_product_to_basket(self):
        self.should_be_name_of_product()
        self.should_be_price_of_product()
        self.should_be_button_add_basket()

        add_to_busket_button = self.browser.find_element(*AddProductPageLocators.BTN_ADD_TO_BASKET)
        add_to_busket_button.click()

        BasePage.solve_quiz_and_get_code(self)
        self.should_be_msg_about_adding()
        self.compare_basket_and_product_price()

