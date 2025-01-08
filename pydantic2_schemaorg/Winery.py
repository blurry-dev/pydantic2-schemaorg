from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.FoodEstablishment import FoodEstablishment


class Winery(FoodEstablishment):
    """A winery.

    See: https://schema.org/Winery
    Model depth: 5
    """

    type_: str = Field(default="Winery", alias="@type", const=True)
