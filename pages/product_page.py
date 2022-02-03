from selenium.common.exceptions import NoAlertPresentException  # в начале файла
from .base_page import BasePage
from .locators import AddProductPageLocators
from .locators import BasePageLocators
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

    def test_guest_cant_see_success_message_after_adding_product_to_basket(self):
        # Открываем страницу товара
        # Добавляем товар в корзину
        self.add_product_to_basket()
        # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
        assert self.is_not_element_present(*AddProductPageLocators.MESSAGE_ABOUT_ADDING), \
            "Есть сообщения об Добавляем товар в корзину"

    def test_guest_cant_see_success_message(self):
        # Открываем страницу товара
        # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
        assert self.is_not_element_present(*AddProductPageLocators.BTN_ADD_TO_BASKET), \
            "Есть кнопка Add basket"

    def test_message_disappeared_after_adding_product_to_basket(self):
        # Открываем страницу товара
        # Добавляем товар в корзину
        self.add_product_to_basket()
        # Проверяем, что нет сообщения об успехе с помощью is_disappeared
        assert self.is_disappeared(*AddProductPageLocators.MESSAGE_ABOUT_ADDING), \
            "Есть сообщения об Добавляем товар в корзину"

    def test_guest_can_go_to_login_page_from_product_page(self):
        assert self.browser.find_element(*BasePageLocators.LOGIN_LINK), "Not should login link"



