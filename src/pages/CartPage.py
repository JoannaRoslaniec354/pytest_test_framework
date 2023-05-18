from test_framework.src.pages.locators.CartLocators import CartLocators
from test_framework.src.SeleniumExtended import SeleniumExtended


class CartPage(CartLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def input_coupon_code(self, code):
        self.sl.wait_and_input_text(self.COUPON_INPUT, code)

    def apply_coupon(self):
        self.sl.wait_and_click_element(self.APPLY_COUPON_BTN)

    def proceed_to_checkout(self):
        self.sl.wait_and_click_element(self.CHECKOUT_BTN)

    def get_names_of_product_in_cart(self):
        product_names_elements = self.sl.wait_and_get_elements(self.PRODUCT_NAME_IN_CART)
        product_names = [i.text for i in product_names_elements]
        return product_names
