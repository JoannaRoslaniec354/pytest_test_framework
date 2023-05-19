from selenium.webdriver.common.by import By


class OrderReceivedLocators:

    ORDER_CONFIRMATION_TITLE = (By.CSS_SELECTOR, 'h1.wp-block-post-title')
    ORDER_NUMBER = (By.CSS_SELECTOR, 'li.order strong')