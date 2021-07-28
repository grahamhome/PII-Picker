from app.web_automation.elements.button import Button
from app.web_automation.elements.checkbox import Checkbox
from app.web_automation.elements.form import Form
from app.web_automation.elements.list_item import ListItem
from app.web_automation.elements.select import Select
from app.web_automation.elements.text_field import TextField
from app.web_automation.page_objects.page import Page


class InteliusHome(Page):
    """
    Interface to the intelius.com homepage. Provides methods to search for PII.
    """

    _url = "https://www.intelius.com/"

    # Page elements

    _name_lookup_tab = ListItem(attribute="id", identifier="name")
    _phone_lookup_tab = ListItem(attribute="id", identifier="phone-number")
    _address_lookup_tab = ListItem(attribute="id", identifier="name")

    _critical_elements = [_name_lookup_tab, _phone_lookup_tab, _address_lookup_tab]

    _name_lookup_form = Form(
        first_name=TextField(attribute="name", identifier="firstName"),
        last_name=TextField(attribute="name", identifier="lastName"),
        city=TextField(attribute="name", identifier="city"),
        state=Select(attribute="name", identifier="state"),
        its_me=Checkbox(attribute="id", identifier="self-search"),
        submit=Button(attribute="type", identifier="submit")
    )

    _phone_lookup_form = Form(
        phone=TextField(attribute="id", identifier="phone"),
        submit=Button(attribute="type", identifier="submit")
    )

    _address_lookup_form = Form(
        street=TextField(attribute="name", identifier="street"),
        city=TextField(attribute="name", identifier="city"),
        state=Select(attribute="name", identifier="state"),
        submit=Button(attribute="type", identifier="submit")
    )