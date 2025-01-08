from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.WebPageElement import WebPageElement


class WPFooter(WebPageElement):
    """The footer section of the page.

    See: https://schema.org/WPFooter
    Model depth: 4
    """

    type_: str = Field(default="WPFooter", alias="@type", const=True)
