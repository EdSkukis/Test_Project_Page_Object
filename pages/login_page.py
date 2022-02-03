from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import BasePageLocators


class LoginPage(BasePage):
    def should_be_login_link(self):
        self.browser.find_element(*BasePageLocators.LOGIN_LINK), "Not should login link"

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        correct_login_url = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
        get_login_url = driver.current_url
        assert correct_login_url==get_login_url, "Login link is not correct"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_USERNAME) and \
               self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD) and \
               self.is_element_present(*LoginPageLocators.LOGIN_BUTTON_LOG_IN), "Login form is not correct"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.LOGIN_REG_USERNAME) and \
               self.is_element_present(*LoginPageLocators.LOGIN_REG_PASSWORD_1) and \
               self.is_element_present(*LoginPageLocators.LOGIN_REG_PASSWORD_2) and \
               self.is_element_present(*LoginPageLocators.LOGIN_BUTTON_LOG_IN), "Regestration form is not correct"

