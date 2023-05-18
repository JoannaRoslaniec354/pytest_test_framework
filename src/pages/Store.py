from test_framework.src.SeleniumExtended import SeleniumExtended
from test_framework.src.helpers.config_helpers import get_base_url
from test_framework.src.pages.locators.StoreLocators import StoreLocators


class Store(StoreLocators):

    def __init__(self, driver):
        self.endpoint = '/shop'
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_store(self):
        base_url = get_base_url()
        store_url = base_url + self.endpoint
        self.driver.get(store_url)

    def add_to_cart(self):
        self.sl.get_all_buttons_and_click_random(self.ADD_TO_CART_BUTTON)

    def view_cart_via_button(self):
        self.sl.wait_and_click_element(self.VIEW_CART)
