"""
Description: Represents an h6 header on a web page.
DEPRECIATED: Use heading.py!
"""

from app.web_automation.elements.heading import Heading


class H6(Heading):
    """
    Represents an h6 header on a web page. Allows elements to be located via different attributes
    e.g. ID or class name.
    """

    def __init__(self, identifier=None, attribute=None, xpath=None):
        """
        Construct a new H6 instance,
        located using the specified attribute and attribute-value OR a supplied xpath.
        """
        super().__init__(element_type="h6", identifier=identifier, attribute=attribute, xpath=xpath)
