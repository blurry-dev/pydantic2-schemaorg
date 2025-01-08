from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.PriceComponentTypeEnumeration import (
    PriceComponentTypeEnumeration,
)


class CleaningFee(PriceComponentTypeEnumeration):
    """Represents the cleaning fee part of the total price for an offered product, for example a vacation rental.

    See: https://schema.org/CleaningFee
    Model depth: 5
    """

    type_: str = Field(default="CleaningFee", alias="@type", const=True)
