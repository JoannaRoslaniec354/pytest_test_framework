from selenium.webdriver.common.by import By


class OrderReceivedLocators:
    ORDER_CONFIRMATION_TITLE = (By.CSS_SELECTOR, 'p.woocommerce-notice')
    ORDER_NUMBER = (By.CSS_SELECTOR, 'li.order strong')
