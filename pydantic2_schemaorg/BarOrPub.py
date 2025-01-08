from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.FoodEstablishment import FoodEstablishment


class BarOrPub(FoodEstablishment):
    """A bar or pub.

    See: https://schema.org/BarOrPub
    Model depth: 5
    """

    type_: str = Field(default="BarOrPub", alias="@type", const=True)
