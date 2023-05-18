import pytest
from selenium import webdriver
import os
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.safari.options import Options as SafariOptions


@pytest.fixture(scope="class")
def init_driver(request):
    supported_browsers = ['chrome', 'safari', 'ch', 's', 'headlesschrome', 'headlesssafari']
    browser = os.environ.get('BROWSER')
    if not browser:
        raise Exception("The environment variable 'BROWSER' must be set")
    browser = browser.lower()
    if browser not in supported_browsers:
        raise Exception('{} not in supported browsers. Supported browsers are: {}'.format(browser, supported_browsers))
    if browser in ('chrome', 'ch'):
        driver = webdriver.Chrome()
    elif browser in ('safari', 's'):
        driver = webdriver.Safari()
    elif browser in 'headlesschrome':
        chrome_options = ChromeOptions()
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_options)

    request.cls.driver = driver
    yield
    driver.quit()
