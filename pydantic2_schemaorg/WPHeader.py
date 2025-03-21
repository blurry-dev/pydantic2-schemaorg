from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.WebPageElement import WebPageElement


class WPHeader(WebPageElement):
    """The header section of the page.

    See: https://schema.org/WPHeader
    Model depth: 4
    """

    type_: str = Field(default="WPHeader", alias="@type", const=True)
