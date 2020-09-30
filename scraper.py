from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from time import sleep


def get_page_iframe(driver, link):
    driver.get(link)
    try:
        iframe = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, 'iframe')))
    except TimeoutException:
        print("Can't find iframe in 10 seconds")
    driver.get(iframe.get_attribute('src'))
    try:
        # check if there is any events, and page is loaded
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, '_24er')))
    except TimeoutException:
        print("Can't find any events in 10 seconds")


def event_info(driver, link):
    # example link = https://www.facebook.com/events/3102548586466148
    main_window_handle = driver.current_window_handle
    driver.execute_script(f'window.open("{link}","_blank");')
    driver.switch_to.window(driver.window_handles[1])

    try:
        title = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "//*[@id='mount_0_0']/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div[2]/h2/span/span/span"))).text
    except TimeoutException:
        print("Can't find any title of event in 10 seconds")

    # find hosts (can be more than one)
    hosts = []
    for h in driver.find_elements_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[4]/div/div[1]/div/div/div[1]/div[1]/div/div/div/div/div/div/div[2]/div/div/span/strong'):
        hosts += [h.text]
    time = driver.find_element_by_xpath(
        "//*[@id='mount_0_0']/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div[1]/h2/span").text
    going = driver.find_element_by_xpath(
        '//*[@id="mount_0_0"]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[4]/div/div[1]/div/div/div[2]/div[2]/div[last()]/div/div/div/div[2]/div/div[1]/div[1]/span[1]').text
    interested = driver.find_element_by_xpath(
        '//*[@id="mount_0_0"]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[4]/div/div[1]/div/div/div[2]/div[2]/div[last()]/div/div/div/div[2]/div/div[2]/div[1]/span[1]').text
    image = driver.find_elements_by_xpath(
        '//*[@id="mount_0_0"]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[1]/div[1]/div/div/div[2]/div/a/div/div/div/div/img')
    if image:
        image = image[0].get_attribute("src")
    location = driver.find_element_by_xpath(
        "//*[@id='mount_0_0']/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div[3]/span/span").text
    ticket = driver.find_elements_by_xpath(
        '//*[@id="mount_0_0"]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[4]/div/div[1]/div/div/div[2]/div[2]/div[1]/div/div/div/div[2]/a')
    if ticket:
        ticket = ticket[0].get_attribute('href')
    details_bottom = driver.find_element_by_xpath(
        "//*[@id='mount_0_0']/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[4]/div/div[1]/div/div/div[1]/div[1]/div/div/div/div[last()]")
    categories = details_bottom.find_element_by_css_selector(
        'div.lhclo0ds').text.split('\n')
    see_more = driver.find_elements_by_xpath(
        '//*[@id="mount_0_0"]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[4]/div/div[1]/div/div/div[1]/div[1]/div/div/div/div/span/div/div')

    # if 'See More', click
    if see_more:
        driver.execute_script("arguments[0].click();", see_more[0])
    sleep(1)
    description = details_bottom.find_element_by_css_selector('span').text
    # if see more, delete 'See Less' from description
    if see_more:
        description = description[:-9]

    driver.close()
    driver.switch_to.window(main_window_handle)
    return {
        "hosts": hosts,
        "title": title,
        "time": time,
        "description": description,
        "location": location,
        "ticket": ticket,
        "link": link,
        "image": image,
        "interested": interested,
        "going": going,
        "categories": categories
    }


def events_upcoming(driver, link=""):
    if link:
        get_page_iframe(driver, link)

    all_events = []
    upcoming_events = driver.find_elements_by_xpath(
        "//*[@class='_4dmd _4eok uiGrid _51mz']")

    for event in upcoming_events:
        event_link = event.find_element_by_css_selector(
            "div._4dmk>a").get_attribute("href")
        all_events += [event_info(driver, event_link)]
        # driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
    return all_events


def events_recurring(driver, link=""):
    if link:
        get_page_iframe(driver, link)

    all_events = []
    recurring_event_id = driver.find_elements_by_id("recurring_events_card")
    if recurring_event_id:
        recurring_events_card = recurring_event_id[0].find_elements_by_xpath(
            "//*[@class='_1b-a _4-u2  _4-u8']")
        for card in recurring_events_card:
            # if there is (+3 | +4 ...) button to see more recurring events
            popup_e = card.find_elements_by_class_name('_2l4u')
            if popup_e:
                driver.execute_script("arguments[0].click();", popup_e[0])
                try:
                    recurring_events = WebDriverWait(driver, 10).until(
                        EC.presence_of_all_elements_located((By.XPATH, "//*[@class='_2pi4 _2rsy']")))
                except TimeoutException:
                    print("Can't find events in recurring events in 10 seconds")
            else:
                recurring_events = card.find_elements_by_class_name('_2l45')
            for e in recurring_events:
                if popup_e:
                    event_link = e.find_element_by_class_name(
                        "_62pa").get_attribute("data-hovercard")
                    event_link = "https://www.facebook.com/events/" + \
                        event_link.split('=')[-1] + "/"

                else:
                    event_link = e.get_attribute("href")
                all_events += [event_info(driver, event_link)]
                # when open new tab, and then close tab, so needs to switch driver to current tab and also inside iframe
                # driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
            if popup_e:
                close_popup = driver.find_element_by_xpath(
                    "//*[@id='facebook']/body/div[8]/div[2]/div/div/div/div[1]/div/div[1]/a")
                driver.execute_script("arguments[0].click();", close_popup)
    return all_events


def events(driver, link):
    # Example: link = 'https://www.facebook.com/page/events/'
    get_page_iframe(driver, link)

    all_events = []

    all_events += events_recurring(driver)

    all_events += events_upcoming(driver)

    ## Switch back to the "default content" (that is, out of the iframes) ##
    # driver.switch_to.default_content()
    driver.close()
    return all_events
