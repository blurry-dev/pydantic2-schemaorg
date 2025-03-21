from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.WebPage import WebPage


class CollectionPage(WebPage):
    """Web page type: Collection page.

    See: https://schema.org/CollectionPage
    Model depth: 4
    """

    type_: str = Field(default="CollectionPage", alias="@type", const=True)
