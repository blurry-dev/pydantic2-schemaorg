from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.FoodEstablishment import FoodEstablishment


class Distillery(FoodEstablishment):
    """A distillery.

    See: https://schema.org/Distillery
    Model depth: 5
    """

    type_: str = Field(default="Distillery", alias="@type", const=True)
