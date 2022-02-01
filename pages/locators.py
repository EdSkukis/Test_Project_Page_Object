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
