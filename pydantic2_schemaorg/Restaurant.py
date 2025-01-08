from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.FoodEstablishment import FoodEstablishment


class Restaurant(FoodEstablishment):
    """A restaurant.

    See: https://schema.org/Restaurant
    Model depth: 5
    """

    type_: str = Field(default="Restaurant", alias="@type", const=True)
