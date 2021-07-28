from app.crawlers.intelius.intelius_results import IntelliusResults
from app.web_automation.elements.div import Div
from app.web_automation.page_objects.page import Page, which_page_loads


class IntelliusSearching(Page):
    """
    Interface to the intelius.com page displayed when a search is in progress.
    """
    _url = "https://www.intelius.com/search/"

    _dont_know_response = Div(attribute="class", identifier="confirm-not-sure")

    _critical_elements = [_dont_know_response]

    def ignore_additional_prompts(self):
        """
        Click "I Don't Know" as many times as necessary to dismiss prompts for additional info.
        :return:
        """
        self._dont_know_response.click()
        return which_page_loads(IntelliusSearching, IntelliusResults)