from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.WebPage import WebPage


class AboutPage(WebPage):
    """Web page type: About page.

    See: https://schema.org/AboutPage
    Model depth: 4
    """

    type_: str = Field(default="AboutPage", alias="@type", const=True)
