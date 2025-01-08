from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.WebPageElement import WebPageElement


class WPSideBar(WebPageElement):
    """A sidebar section of the page.

    See: https://schema.org/WPSideBar
    Model depth: 4
    """

    type_: str = Field(default="WPSideBar", alias="@type", const=True)
