# facebook_events_scraper

### driver(pathToChromeDriver)

- You can write your own selenium webdriver code or use the module's driver function

- example:
  `driver = facebook_events_scraper.driver("chromedriver")`

### event_info(driver, link="")

- Example: event_info(driver, "https://www.facebook.com/events/310254858646618")
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

- Example: events_upcoming(driver, "https://www.facebook.com/pagename/events/")
- Example: events_recurring(driver, "https://www.facebook.com/pagename/events/")
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

- Example: events(driver, "https://www.facebook.com/pagename/events/")
- The function returns a list of dictionaries

```
return [events_upcoming(driver, link) + events_recurring(driver, link)]
```

### Preview

[![event_info](https://thumbs.gfycat.com/UncommonPoliteIchthyostega-size_restricted.gif)](https://giant.gfycat.com/UncommonPoliteIchthyostega.mp4)
[![event_recurring](https://thumbs.gfycat.com/WideeyedLoathsomeBanteng-size_restricted.gif)](https://giant.gfycat.com/WideeyedLoathsomeBanteng.mp4)
[![event_upcoming](https://thumbs.gfycat.com/ReliableWarlikeBobcat-size_restricted.gif)](https://giant.gfycat.com/ReliableWarlikeBobcat.mp4)
