from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.WebPage import WebPage


class SearchResultsPage(WebPage):
    """Web page type: Search results page.

    See: https://schema.org/SearchResultsPage
    Model depth: 4
    """

    type_: str = Field(default="SearchResultsPage", alias="@type", const=True)
