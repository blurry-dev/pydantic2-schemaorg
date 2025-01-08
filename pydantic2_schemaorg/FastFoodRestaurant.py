from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.FoodEstablishment import FoodEstablishment


class FastFoodRestaurant(FoodEstablishment):
    """A fast-food restaurant.

    See: https://schema.org/FastFoodRestaurant
    Model depth: 5
    """

    type_: str = Field(default="FastFoodRestaurant", alias="@type", const=True)
