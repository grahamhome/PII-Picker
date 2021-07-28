from app.web_automation.page_objects.page import Page


class IntelliusResults(Page):
    """
    Interface to the results page for intellius.com. Enables data scraping from results.
    """

    _url = "https://www.intelius.com/results/"