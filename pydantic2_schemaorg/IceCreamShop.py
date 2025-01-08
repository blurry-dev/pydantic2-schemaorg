from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.FoodEstablishment import FoodEstablishment


class IceCreamShop(FoodEstablishment):
    """An ice cream shop.

    See: https://schema.org/IceCreamShop
    Model depth: 5
    """

    type_: str = Field(default="IceCreamShop", alias="@type", const=True)
