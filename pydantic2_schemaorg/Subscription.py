from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.PriceComponentTypeEnumeration import (
    PriceComponentTypeEnumeration,
)


class Subscription(PriceComponentTypeEnumeration):
    """Represents the subscription pricing component of the total price for an offered product.

    See: https://schema.org/Subscription
    Model depth: 5
    """

    type_: str = Field(default="Subscription", alias="@type", const=True)
