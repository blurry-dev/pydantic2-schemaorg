from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.FoodEstablishment import FoodEstablishment


class Brewery(FoodEstablishment):
    """Brewery.

    See: https://schema.org/Brewery
    Model depth: 5
    """

    type_: str = Field(default="Brewery", alias="@type", const=True)
