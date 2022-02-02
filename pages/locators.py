from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    # Login
    LOGIN_USERNAME = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_BUTTON_LOG_IN = (By.CSS_SELECTOR, "#login_form > button")

    # Regestration
    LOGIN_REG_USERNAME = (By.CSS_SELECTOR, "#id_registration-email")
    LOGIN_REG_PASSWORD_1 = (By.CSS_SELECTOR, "#id_registration-password1")
    LOGIN_REG_PASSWORD_2 = (By.CSS_SELECTOR, "#id_registration-password2")
    LOGIN_BUTTON_LOG_IN = (By.CSS_SELECTOR, "#register_form > button")

class AddProductPageLocators():
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, '#add_to_basket_form > button')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main > h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.price_color:nth-child(2)')


    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, 'div.alert:nth-child(1) strong')
    BASKET_PRICE = (By.CSS_SELECTOR, '.alertinner p strong')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

