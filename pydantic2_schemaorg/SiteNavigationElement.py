from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.WebPageElement import WebPageElement


class SiteNavigationElement(WebPageElement):
    """A navigation element of the page.

    See: https://schema.org/SiteNavigationElement
    Model depth: 4
    """

    type_: str = Field(default="SiteNavigationElement", alias="@type", const=True)
