from test_framework.src.SeleniumExtended import SeleniumExtended
from test_framework.src.pages.locators.MyAccountSignedOutLocators import MyAccountSignedOutLocators
from test_framework.src.helpers.config_helpers import get_base_url
import logging as logger


class MyAccountSignedOut(MyAccountSignedOutLocators):
    endpoint = '/my-account/'

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_my_account(self):
        base_url = get_base_url()
        my_account_url = base_url + self.endpoint
        logger.info(f"Going to: {my_account_url}")
        self.driver.get(my_account_url)

    def input_username(self, username):
        self.sl.wait_and_input_text(self.LOGIN_USERNAME_INPUT, username)

    def input_password(self, password):
        self.sl.wait_and_input_text(self.LOGIN_PASSWORD_INPUT, password)

    def click_login_button(self):
        logger.debug(f'Clicking {self.LOGIN_BUTTON}')
        self.sl.wait_and_click_element(self.LOGIN_BUTTON)

    def text_message(self, err_msg):
        self.sl.wait_and_see_msg(self.ERROR_MSSG, err_msg)

    def register_send_email(self, login):
        self.sl.wait_and_input_text(self.REGISTER_EMAIL, login)

    def register_send_pass(self, password):
        self.sl.wait_and_input_text(self.REGISTER_PASS, password)

    def click_register_button(self):
        self.sl.wait_and_click_element(self.REGISTER_BUTTON)
