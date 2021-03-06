from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    # Login
    LOGIN_USERNAME = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_BUTTON_LOG_IN = (By.CSS_SELECTOR, "#login_form > button")

    LOGIN_NEW_USER_OK = (By.CSS_SELECTOR,'#messages > div > div')
    USER_IS_LOGIN = (By.CSS_SELECTOR,'#logout_link')

    # Regestration
    LOGIN_REG_USERNAME = (By.CSS_SELECTOR, "#id_registration-email")
    LOGIN_REG_PASSWORD_1 = (By.CSS_SELECTOR, "#id_registration-password1")
    LOGIN_REG_PASSWORD_2 = (By.CSS_SELECTOR, "#id_registration-password2")
    LOGIN_BUTTON_LOG_IN = (By.CSS_SELECTOR, "#register_form > button")

class AddProductPageLocators():
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, '#add_to_basket_form > button')
    PRODUCT_NAME = (By.CSS_SELECTOR, '#content_inner > article > div.row > div.col-sm-6.product_main > h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.price_color:nth-child(2)')


    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, 'div.alert:nth-child(1) strong')
    BASKET_PRICE = (By.CSS_SELECTOR, '.alertinner p strong')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class BasketPageLocator():
    SUB_HEAD = (By.CSS_SELECTOR, "#promotions > section:nth-child(1) > div > h2")
    SUB_HEAD_BASKET = (By.CSS_SELECTOR, '#write_review')
    BTN_BASKET = (By.CSS_SELECTOR, '#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a')
    BASKET_EMPTY_TEXT = (By.CSS_SELECTOR, '#content_inner > p')
    BASKET_NOT_EMPTY = (By.CSS_SELECTOR,'#content_inner > div.basket-title.hidden-xs > div > h2')

