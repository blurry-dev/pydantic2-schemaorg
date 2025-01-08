from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.LocalBusiness import LocalBusiness


class ShoppingCenter(LocalBusiness):
    """A shopping center or mall.

    See: https://schema.org/ShoppingCenter
    Model depth: 4
    """

    type_: str = Field(default="ShoppingCenter", alias="@type", const=True)
