from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from time import sleep
from dateutil import parser
from datetime import date, timedelta


def _multiple_classes(class_names):
    return " and ".join(
        [f"contains(@class, '{class_name}')" for class_name in class_names.split()]
    )


def _recurring_event(driver):
    recurring_event = driver.find_elements_by_xpath(
        "//a[@aria-label='[object Object]']"
    )
    if len(recurring_event) >= 3:
        next_event = recurring_event[-1].get_attribute("href")
    else:
        next_event = ""
    print("NEXT EVENT", next_event)
    return next_event


def _time_converter(time):
    at_count = time.count(" at")
    today = date.today()
    if "today" in time:
        # TODAY AT 7:30 PM
        time = time.replace("today", today.strftime("%B %d, %Y"))
    elif "tomorrow" in time:
        # TOMORROW AT 9 AM
        time = time.replace(
            "tomorrow", (today + timedelta(days=1)).strftime("%B %d, %Y")
        )
    if at_count == 1:
        # If there is end date/time
        # TODAY AT 9 AM – 9 PM
        if time.count(" –") == 1:
            sliced_date, sliced_time = time.split(" at")
            start, end = sliced_time.split(" –")
            start_datetime = parser.parse(sliced_date + start)
            end_datetime = parser.parse(sliced_date + end)
        else:
            # MONDAY AT 8 PM
            start_datetime = end_datetime = parser.parse(time)
    elif at_count == 2 and time.count("–") == 1:
        # DEC 25 AT 12 PM – DEC 26 AT 8 PM
        start, end = time.split("–")
        start_datetime = parser.parse(start)
        end_datetime = parser.parse(end)

    return [start_datetime, end_datetime]


# scrape one individual event
def event_info(driver, link):
    # example link = https://www.facebook.com/events/3102548586466148
    event_id = link.split("/")[4]
    link = "https://www.facebook.com/events/" + event_id
    main_window_handle = driver.current_window_handle
    driver.execute_script(f'window.open("{link}","_blank");')
    driver.switch_to.window(driver.window_handles[1])
    driver.get_screenshot_as_file("hi.png")
    try:
        title = (
            WebDriverWait(driver, 5)
            .until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        f"//span[{_multiple_classes('d2edcug0 hpfvmrgz qv66sw1b c1et5uql oi732d6d ik7dh3pa ht8s03o8 a8c37x1j keod5gw0 nxhoafnm aigsh9s9 fe6kdd0r mau55g9w c8b282yb ns63r2gh rwim8176 m6dqt4wy h7mekvxk hnhda86s oo9gr5id hzawbc8m')}]",
                    )
                )
            )
            .text
        )
    except TimeoutException:
        next_event = _recurring_event(driver)
        driver.close()
        driver.switch_to.window(main_window_handle)
        print("Can't find the event title in 5 seconds")
        return None, next_event

    location = driver.find_element_by_xpath(
        f"//*[{_multiple_classes('d2edcug0 hpfvmrgz qv66sw1b c1et5uql oi732d6d ik7dh3pa ht8s03o8 a8c37x1j keod5gw0 nxhoafnm aigsh9s9 fe6kdd0r mau55g9w c8b282yb d9wwppkn iv3no6db a5q79mjw g1cxx5fr b1v8xokw m9osqain hzawbc8m')}]"
    ).text
    time = driver.find_element_by_xpath(
        f"//h2[{_multiple_classes('gmql0nx0 l94mrbxd p1ri9a11 lzcic4wl d2edcug0 hpfvmrgz')}]/span[{_multiple_classes('d2edcug0 hpfvmrgz qv66sw1b c1et5uql oi732d6d ik7dh3pa ht8s03o8 a8c37x1j keod5gw0 nxhoafnm aigsh9s9 fe6kdd0r mau55g9w c8b282yb d9wwppkn iv3no6db jq4qci2q a3bd9o3v hnhda86s jdix4yx3 hzawbc8m')}]"
    ).text
    image = driver.find_elements_by_xpath(
        "//*[@data-imgperflogname='profileCoverPhoto']"
    )
    if image:
        image = image[0].get_attribute("src")
    # find hosts (can be more than one)
    hosts = []
    for h in driver.find_elements_by_xpath(
        f"//strong/a[{_multiple_classes('oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl oo9gr5id gpro0wi8 lrazzd5p')}]"
    ):
        hosts += [h.text]
    print(hosts)
    categories = driver.find_elements_by_xpath(
        f"//*[{_multiple_classes('d2edcug0 hpfvmrgz qv66sw1b c1et5uql oi732d6d ik7dh3pa ht8s03o8 a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d9wwppkn fe6kdd0r mau55g9w c8b282yb mdeji52x e9vueds3 j5wam9gi lrazzd5p oo9gr5id')}]"
    )
    if categories:
        categories = categories[0].text.split("\n")
    see_more = driver.find_elements_by_xpath(
        f"//div[{_multiple_classes('oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl oo9gr5id gpro0wi8 lrazzd5p')}][@role='button'][contains(text(),'See more')]"
    )

    # if 'See More', click
    if see_more:
        driver.execute_script("arguments[0].click();", see_more[0])
        sleep(1)
    description = driver.find_element_by_xpath(
        f"//div[@class='p75sslyk']/span[{_multiple_classes('d2edcug0 hpfvmrgz qv66sw1b c1et5uql oi732d6d ik7dh3pa ht8s03o8 a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d9wwppkn fe6kdd0r mau55g9w c8b282yb iv3no6db jq4qci2q a3bd9o3v b1v8xokw oo9gr5id')}]"
    ).text
    # if see more, delete 'See Less' from description
    if see_more:
        description = description[:-9]

    ticket = driver.find_elements_by_xpath("//a[@aria-label='Find Tickets']")
    if ticket:
        ticket = ticket[0].get_attribute("href")
    else:
        ticket = ""
    start_datetime, end_datetime = _time_converter(time.replace(" UTC+07", "").lower())
    if start_datetime != end_datetime:
        time = f"{start_datetime.strftime('%X')[:-3]} - {end_datetime.strftime('%H:%M %d/%m/%Y')}"
    else:
        time = end_datetime.strftime("%H:%M %d/%m/%Y")
    start_datetime = start_datetime.strftime("%Y-%m-%dT%H:%M:%SZ")
    end_datetime = end_datetime.strftime("%Y-%m-%dT%H:%M:%SZ")

    next_event = _recurring_event(driver)

    driver.close()
    driver.switch_to.window(main_window_handle)
    return (
        {
            "_id": event_id,
            "hosts": hosts,
            "title": title,
            "time": time,
            "description": description,
            "location": location,
            "link": link,
            "image": image,
            "categories": categories,
            "start_time": start_datetime,
            "end_time": end_datetime,
            "ticket": ticket,
        },
        next_event,
    )


# scrape the upcoming events section in facebook.com/pagename/events
def events_upcoming(driver, link=""):
    all_events = []
    driver.get(link)
    sleep(2)

    driver.get_screenshot_as_file("hi.png")
    upcoming_events_sec = driver.find_elements_by_xpath(
        f"//div[{_multiple_classes('dati1w0a ihqw7lf3 hv4rvrfc discj3wi')}]"
    )

    see_more = driver.find_elements_by_xpath(
        f"//div[{_multiple_classes('oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 pq6dq46d p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl n00je7tq arfg74bv qs9ysxi8 k77z8yql l9j0dhe7 abiwlrkh p8dawk7l cbu4d94t taijpn5t k4urcfbm')}][@aria-label='See more']"
    )
    if see_more:
        driver.execute_script("arguments[0].click();", see_more[0])
        sleep(1)
    if upcoming_events_sec:
        upcoming_events = upcoming_events_sec[0].find_elements_by_css_selector(
            "a[class='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 gpro0wi8 hnhda86s']"
        )
        if (
            upcoming_events
            and upcoming_events[0]
            .find_elements_by_xpath("//*[@aria-selected='true']")[-1]
            .text
            == "Upcoming"
        ):
            # weird events layout
            upcoming_events = upcoming_events_sec[0].find_elements_by_xpath(
                f"//div[{_multiple_classes('buofh1pr hv4rvrfc')}]/div/a[{_multiple_classes('oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 gpro0wi8')}]"
            )
        for event in upcoming_events:
            event_link = event.get_attribute("href")
            if event_link[-6:] == "events":
                break
            info, next_event_link = event_info(driver, event_link)
            if isinstance(info, dict):
                all_events.append(info)
            if next_event_link:
                for i in range(3):
                    info, next_event_link = event_info(driver, next_event_link)
                    if isinstance(info, dict):
                        all_events.append(info)
                    if not next_event_link:
                        break
    return all_events
