from selenium.webdriver.common.by import By


class MyAccountSignedOutLocators:
    LOGIN_USERNAME_INPUT = (By.ID, 'username')
    LOGIN_PASSWORD_INPUT = (By.ID, 'password')
    LOGIN_BUTTON = (By.NAME, 'login')
    ERROR_MSSG = (By.CSS_SELECTOR, 'ul.woocommerce-error')
    REGISTER_EMAIL = (By.ID, 'reg_email')
    REGISTER_PASS = (By.ID, 'reg_password')
    REGISTER_BUTTON = (By.NAME, 'register')
