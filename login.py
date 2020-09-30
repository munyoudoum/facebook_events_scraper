def login(driver, email, password):
    driver.get('https://www.facebook.com')
    # find the username field and enter the email example@yahoo.com.
    username = driver.find_elements_by_css_selector("input[name=email]")
    username[0].send_keys(email)
    # find the password field and enter the password password.
    password = driver.find_elements_by_css_selector("input[name=pass]")
    password[0].send_keys(password)
    # find the login button and click it.
    loginButton = driver.find_elements_by_css_selector("button[type=submit]")
    loginButton[0].click()
