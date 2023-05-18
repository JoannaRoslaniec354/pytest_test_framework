from selenium.webdriver.common.by import By


class CheckoutLocators:

    BILLING_FIRST_NAME_INPUT = (By.ID, 'billing_first_name')
    BILLING_LAST_NAME_INPUT = (By.ID, 'billing_last_name')
    COUNTRY_DROPDOWN = (By.ID, 'select2-billing_country-container')
    COUNTRY_SEARCH_INPUT = (By.CSS_SELECTOR, 'input.select2-search__field')
    STREET_ADDRESS_INPUT = (By.ID, 'billing_address_1')
    POSTCODE_INPUT = (By.ID, 'billing_postcode')
    CITY_INPUT = (By.ID, 'billing_city')
    PHONE_INPUT = (By.ID, 'billing_phone')
    EMAIL_INPUT = (By.ID, 'billing_email')
    FINAL_PRICE = (By.CSS_SELECTOR, '')
    PLACE_ORDER_BTN = (By.ID, 'place_order')