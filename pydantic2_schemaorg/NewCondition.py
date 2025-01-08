from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.OfferItemCondition import OfferItemCondition


class NewCondition(OfferItemCondition):
    """Indicates that the item is new.

    See: https://schema.org/NewCondition
    Model depth: 5
    """

    type_: str = Field(default="NewCondition", alias="@type", const=True)
