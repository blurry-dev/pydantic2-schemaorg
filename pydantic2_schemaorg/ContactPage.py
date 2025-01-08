from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.WebPage import WebPage


class ContactPage(WebPage):
    """Web page type: Contact page.

    See: https://schema.org/ContactPage
    Model depth: 4
    """

    type_: str = Field(default="ContactPage", alias="@type", const=True)
