from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.WebPage import WebPage


class ProfilePage(WebPage):
    """Web page type: Profile page.

    See: https://schema.org/ProfilePage
    Model depth: 4
    """

    type_: str = Field(default="ProfilePage", alias="@type", const=True)
