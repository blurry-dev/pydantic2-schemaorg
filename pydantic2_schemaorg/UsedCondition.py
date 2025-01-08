from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.OfferItemCondition import OfferItemCondition


class UsedCondition(OfferItemCondition):
    """Indicates that the item is used.

    See: https://schema.org/UsedCondition
    Model depth: 5
    """

    type_: str = Field(default="UsedCondition", alias="@type", const=True)
