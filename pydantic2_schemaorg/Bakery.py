from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.FoodEstablishment import FoodEstablishment


class Bakery(FoodEstablishment):
    """A bakery.

    See: https://schema.org/Bakery
    Model depth: 5
    """

    type_: str = Field(default="Bakery", alias="@type", const=True)
