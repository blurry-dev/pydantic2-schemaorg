from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.WebPage import WebPage


class CheckoutPage(WebPage):
    """Web page type: Checkout page.

    See: https://schema.org/CheckoutPage
    Model depth: 4
    """

    type_: str = Field(default="CheckoutPage", alias="@type", const=True)
