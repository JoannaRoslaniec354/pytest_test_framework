from test_framework.src.SeleniumExtended import SeleniumExtended
from test_framework.src.pages.locators.MyAccountSignedInLocators import MyAccountSignedInLocators


class MyAccountSignedIn(MyAccountSignedInLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def welcome_text_visible(self, text):
        self.sl.wait_and_see_msg(self.HELLO_MSG, text)
