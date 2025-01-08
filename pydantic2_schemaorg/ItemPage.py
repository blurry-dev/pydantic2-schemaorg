from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.WebPage import WebPage


class ItemPage(WebPage):
    """A page devoted to a single item, such as a particular product or hotel.

    See: https://schema.org/ItemPage
    Model depth: 4
    """

    type_: str = Field(default="ItemPage", alias="@type", const=True)
