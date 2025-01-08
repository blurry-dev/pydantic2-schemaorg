from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.FoodEstablishment import FoodEstablishment


class CafeOrCoffeeShop(FoodEstablishment):
    """A cafe or coffee shop.

    See: https://schema.org/CafeOrCoffeeShop
    Model depth: 5
    """

    type_: str = Field(default="CafeOrCoffeeShop", alias="@type", const=True)
