from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Enumeration import Enumeration


class OfferItemCondition(Enumeration):
    """A list of possible conditions for the item.

    See: https://schema.org/OfferItemCondition
    Model depth: 4
    """

    type_: str = Field(default="OfferItemCondition", alias="@type", const=True)
