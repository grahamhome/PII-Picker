"""
Defines a map of all tag names to their corresponding PageElement classes
"""
from selenium.webdriver.remote.webelement import WebElement

from app.web_automation.elements.anchor import Anchor
from app.web_automation.elements.date_picker import DatePicker
from app.web_automation.elements.dropdown_option import DropdownOption
from app.web_automation.elements.file_picker import FilePicker
from app.web_automation.elements.page_element import PageElement
from app.web_automation.elements.button import Button
from app.web_automation.elements.canvas import Canvas
from app.web_automation.elements.checkbox import Checkbox
from app.web_automation.elements.div import Div
from app.web_automation.elements.dropdown import Dropdown
from app.web_automation.elements.form import Form
from app.web_automation.elements.h1 import H1
from app.web_automation.elements.h2 import H2
from app.web_automation.elements.h3 import H3
from app.web_automation.elements.h4 import H4
from app.web_automation.elements.img import Img
from app.web_automation.elements.italic import Italic
from app.web_automation.elements.radio_button import RadioButton
from app.web_automation.elements.select import Select
from app.web_automation.elements.table import Table
from app.web_automation.elements.table_foot import TableFoot
from app.web_automation.elements.table_row import TableRow
from app.web_automation.elements.table_data import TableData
from app.web_automation.elements.table_head import TableHead
from app.web_automation.elements.table_body import TableBody

from typing import List, Tuple

from app.web_automation.elements.text_field import TextField

element_map = {
    "a": Anchor,
    "button": Button,
    "canvas": Canvas,
    "div": Div,
    "select": Dropdown,
    "option": DropdownOption,
    "select": Select,
    "form": Form,
    "h1": H1,
    "h2": H2,
    "h3": H3,
    "h4": H4,
    "img": Img,
    "i": Italic,
    "table": Table,
    "tr": TableRow,
    "td": TableData,
    "thead": TableHead,
    "tbody": TableBody,
    "tfoot": TableFoot,
}

input_type_element_map = {
    "text": TextField,
    "tel": TextField,
    "password": TextField,
    "email": TextField,
    "url": TextField,
    "number": TextField,
    "search": TextField,
    "checkbox": Checkbox,
    "submit": Button,
    "button": Button,
    "reset": Button,
    "radio": RadioButton,
    "date": DatePicker,
    "file": FilePicker,
}


def map_elements(element_list: List[Tuple[WebElement, str]]) -> List[PageElement]:
    page_elements = []
    for element_and_xpath in element_list:
        element, xpath = element_and_xpath
        if element.tag_name == "input":
            input_type = element.get_attribute("type")
            pe_class = input_type_element_map.get(input_type, None)
        else:
            pe_class = element_map.get(element.tag_name, None)
        if pe_class:
            page_elements.append(pe_class(xpath=xpath))
        else:
            page_elements.append(PageElement(xpath=xpath))
    return page_elements
