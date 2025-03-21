from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.PriceComponentTypeEnumeration import (
    PriceComponentTypeEnumeration,
)


class ActivationFee(PriceComponentTypeEnumeration):
    """Represents the activation fee part of the total price for an offered product, for example a cellphone contract.

    See: https://schema.org/ActivationFee
    Model depth: 5
    """

    type_: str = Field(default="ActivationFee", alias="@type", const=True)
