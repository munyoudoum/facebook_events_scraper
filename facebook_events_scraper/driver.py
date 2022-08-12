from selenium import webdriver
# from selenium.webdriver.chrome.options import Options


def driver(chromedriver_path, headless=False):
    # use options to save browser cookies
    # options = Options()
    options = webdriver.ChromeOptions()
    # options.add_argument("--profile-directory=Default")
    options.add_argument("--window-size=1325x744")
    if headless:
        options.add_argument('--headless')
    options.add_argument("user-data-dir=selenium")
    driver = webdriver.Chrome(chromedriver_path, chrome_options=options)
    return driver
