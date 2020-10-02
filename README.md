# facebook_events_scraper

## Install

`pip install facebook_events_scraper`

## Usage

```
import facebook_events_scraper as fes
fes.driver(chromedriver)
fes.login(email, password)
fes.event_info(driver, link="")
fes.events_recurring(driver, link="")
fes.events_upcoming(driver, link="")
fes.events(driver, link="")
```

### driver(pathToChromeDriver)

- You can write your own selenium webdriver code, and also use other browser drivers
- Or, you can use the package's driver function
- To download Chromedriver: https://chromedriver.chromium.org/downloads
- example:
  `driver = facebook_events_scraper.driver("chromedriver")`

### login(email, password)

- If you use the package's driver, you only needs to login once because it creates selenium folder which will save the Chrome cookies, the settings, extensions, etc, and the logins done in the previous session are present here.
- Example: `facebook_events_scraper.login("myemail@gmail.com", "mypassword")`
  i

### event_info(driver, link="")

- Example: `facebook_events_scraper.event_info(driver, "https://www.facebook.com/events/310254858646618")`
- The function returns one dictionary

```
return {
    "hosts": ["...", "...", ....],
    "title": "...",
    "time": "...",
    "description": "...",
    "location": "...",
    "ticket": "...",
    "link": "...",
    "image": "...",
    "interested": "...",
    "going": "...",
    "categories": ["...", "...", ....]
}
```

### events_upcoming(driver, link="") and events_recurring(driver, link="")

- Example: `facebook_events_scraper.events_upcoming(driver, "https://www.facebook.com/pagename/events/")`
- Example: `facebook_events_scraper.events_recurring(driver, "https://www.facebook.com/pagename/events/")`
- The function returns a list of dictionaries

```
return [
    {
        "hosts": ["...", "...", ....],
        "title": "...",
        "time": "...",
        "description": "...",
        "location": "...",
        "ticket": "...",
        "link": "...",
        "image": "...",
        "interested": "...",
        "going": "...",
        "categories": ["...", "...", ....]
    },
    {
        "hosts": ["...", ...],
        "title": "...",
        ...
        ...
        ...
    },
    ...
    ...
    ...
]
```

### events(driver, link="")

- Example: `facebook_events_scraper.events(driver, "https://www.facebook.com/pagename/events/")`
- The function returns a list of dictionaries

```
return [events_upcoming(driver, link) + events_recurring(driver, link)]
```

- Note: All the scraping function only works when the facebook layout is the same as when the browser is maximized

## Preview

[![event_info](https://thumbs.gfycat.com/UncommonPoliteIchthyostega-size_restricted.gif)](https://giant.gfycat.com/UncommonPoliteIchthyostega.mp4)
[![event_recurring](https://thumbs.gfycat.com/WideeyedLoathsomeBanteng-size_restricted.gif)](https://giant.gfycat.com/WideeyedLoathsomeBanteng.mp4)
[![event_upcoming](https://thumbs.gfycat.com/ReliableWarlikeBobcat-size_restricted.gif)](https://giant.gfycat.com/ReliableWarlikeBobcat.mp4)
