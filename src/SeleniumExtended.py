import pdb
from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random


class SeleniumExtended:

    def __init__(self, driver):
        self.driver = driver
        self.custom_timeout = 10

    def wait_and_input_text(self, locator, text, timeout=None):
        timeout = timeout if timeout else self.custom_timeout
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator)
                                                  ).send_keys(text)

    def wait_and_click_element(self, locator, timeout=None):
        timeout = timeout if timeout else self.custom_timeout
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator)).click()

    def wait_and_see_msg(self, locator, text, timeout=None):
        timeout = timeout if timeout else self.custom_timeout
        WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element(locator, text))

    def get_all_buttons_and_click_random(self, locator, timeout=None):
        timeout = timeout if timeout else self.custom_timeout
        elements = WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))
        elements[random.randint(0, len(elements))].click()

    def wait_and_input_text_press_enter(self, locator, text, timeout=None):
        timeout = timeout if timeout else self.custom_timeout
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator)
                                                  ).send_keys(text + Keys.ENTER)

    def wait_until_element_clickable_and_click(self, locator, timeout=None):
        timeout = timeout if timeout else self.custom_timeout
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator)).click()
