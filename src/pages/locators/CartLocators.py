from selenium.webdriver.common.by import By


class CartLocators:
    COUPON_INPUT = (By.ID, 'coupon_code')
    APPLY_COUPON_BTN = (By.CSS_SELECTOR, 'button[value="Apply coupon"]')
    CHECKOUT_BTN = (By.CSS_SELECTOR, 'a.checkout-button')

