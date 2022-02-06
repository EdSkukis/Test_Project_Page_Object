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
        correct_login_url = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
        get_login_url = self.browser.current_url
        assert correct_login_url==get_login_url, f"Login link is not correct {get_login_url}"

    def should_be_user_is_login(self):
        assert self.browser.find_element(*LoginPageLocators.USER_IS_LOGIN), "User not logIN"

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

    def should_be_register_new_user(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_NEW_USER_OK), 'Not corregt registration'

    def register_new_user(self, email, password):
        self.should_be_login_url()
        self.should_be_register_form()
        email_url = self.browser.find_element(*LoginPageLocators.LOGIN_REG_USERNAME)
        password_url_1 = self.browser.find_element(*LoginPageLocators.LOGIN_REG_PASSWORD_1)
        password_url_2 = self.browser.find_element(*LoginPageLocators.LOGIN_REG_PASSWORD_2)
        log_in_button = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON_LOG_IN)

        email_url.send_keys(email)
        password_url_1.send_keys(password)
        password_url_2.send_keys(password)
        log_in_button.click()

        self.should_be_register_new_user()




