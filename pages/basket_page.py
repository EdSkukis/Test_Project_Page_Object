from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from .base_page import BasePage
from .locators import BasketPageLocator
from selenium.webdriver.common.by import By


class BasketPage(BasePage):
    def should_be_head_link(self):
        head_text = self.browser.find_element(*BasketPageLocator.SUB_HEAD).text
        assert head_text == 'Welcome!', "Not Head page"

    def should_be_head_link(self):
        assert self.browser.find_element(*BasketPageLocator.SUB_HEAD_BASKET), 'Not product page'

    def should_be_button_basket(self):
        assert self.browser.find_element(*BasketPageLocator.BTN_BASKET), "Basket button not presented"

    def check_basket_is_empty_text(self):
        flag = False
        basket_text = self.browser.find_element(*BasketPageLocator.BASKET_EMPTY_TEXT).text
        if 'empty' in basket_text:
            flag = True
        assert flag, f"Basket not empty: {basket_text}"

    def check_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocator.BASKET_NOT_EMPTY) == False, "Товар уже есть"


    def guest_cant_see_product_in_basket_opened_from_main_page(self):
        # Гость открывает главную страницу
        self.should_be_head_link()

        # Переходит в корзину по кнопке в шапке сайта
        self.should_be_button_basket()
        busket_button = self.browser.find_element(*BasketPageLocator.BTN_BASKET)
        busket_button.click()

        # Ожидаем, что в корзине нет товаров
        self.check_basket_is_empty()
        # Ожидаем, что есть текст о том что корзина пуста
        self.check_basket_is_empty_text()

    def guest_cant_see_product_in_basket_opened_from_product_page(self):
        # Гость открывает страницу товара
        self.should_be_head_link()
        # Переходит в корзину по кнопке в шапке
        self.should_be_button_basket()
        busket_button = self.browser.find_element(*BasketPageLocator.BTN_BASKET)
        busket_button.click()
        # Ожидаем, что в корзине нет товаров
        self.check_basket_is_empty()
        # Ожидаем, что есть текст о том что корзина пуста
        self.check_basket_is_empty_text()
