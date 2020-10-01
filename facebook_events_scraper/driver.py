from selenium import webdriver


def driver(chromedriver_path):
    # use options to save browser cookies
    options = webdriver.ChromeOptions()
    options.add_argument("user-data-dir=selenium")
    driver = webdriver.Chrome(chromedriver_path, options=options)
    return driver
