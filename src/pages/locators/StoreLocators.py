from selenium.webdriver.common.by import By


class StoreLocators:
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, 'a.product_type_simple.add_to_cart_button')
    VIEW_CART = (By.CSS_SELECTOR, '.added_to_cart.wc-forward')