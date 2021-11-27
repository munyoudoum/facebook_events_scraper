from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def driver(chromedriver_path, headless=True):
    # use options to save browser cookies
    options = Options()
    options.add_argument("user-data-dir=selenium")
    if headless:
        options.headless = True
    driver = webdriver.Chrome(chromedriver_path, options=options)
    return driver
