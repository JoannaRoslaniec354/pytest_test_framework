from test_framework.src.SeleniumExtended import SeleniumExtended
from test_framework.src.pages.locators.OrderReceivedLocators import OrderReceivedLocators


class OrderReceived(OrderReceivedLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def verify_order_received_title(self, text):
        self.sl.wait_and_see_msg(self.ORDER_CONFIRMATION_TITLE, text)

    def get_order_number(self):
        return self.sl.wait_and_get_text(self.ORDER_NUMBER)

    def get_text(self):
        return self.sl.wait_and_get_text(self.ORDER_CONFIRMATION_TITLE)