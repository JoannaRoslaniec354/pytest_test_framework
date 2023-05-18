from selenium.webdriver import Keys

from test_framework.src.SeleniumExtended import SeleniumExtended
from test_framework.src.pages.locators.CheckoutLocators import CheckoutLocators


class CheckoutPage(CheckoutLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def fill_form(self, first_name, last_name, address, postcode, phone, email, city):
        self.sl.wait_and_input_text(self.BILLING_FIRST_NAME_INPUT, first_name)
        self.sl.wait_and_input_text(self.BILLING_LAST_NAME_INPUT, last_name)
        self.sl.wait_and_input_text(self.STREET_ADDRESS_INPUT, address)
        self.sl.wait_and_input_text(self.POSTCODE_INPUT, postcode)
        self.sl.wait_and_input_text(self.PHONE_INPUT, phone)
        self.sl.wait_and_input_text(self.EMAIL_INPUT, email)
        self.sl.wait_and_input_text(self.CITY_INPUT, city)

    def chose_country(self, text):
        self.sl.wait_and_click_element(self.COUNTRY_DROPDOWN)
        self.sl.wait_and_input_text_press_enter(self.COUNTRY_SEARCH_INPUT, text)

    def place_order(self):
        self.sl.wait_and_click_element(self.PLACE_ORDER_BTN)
