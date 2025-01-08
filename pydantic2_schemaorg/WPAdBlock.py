from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.WebPageElement import WebPageElement


class WPAdBlock(WebPageElement):
    """An advertising section of the page.

    See: https://schema.org/WPAdBlock
    Model depth: 4
    """

    type_: str = Field(default="WPAdBlock", alias="@type", const=True)
