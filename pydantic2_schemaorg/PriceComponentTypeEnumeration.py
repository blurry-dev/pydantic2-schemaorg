from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Enumeration import Enumeration


class PriceComponentTypeEnumeration(Enumeration):
    """Enumerates different price components that together make up the total price for an offered product.

    See: https://schema.org/PriceComponentTypeEnumeration
    Model depth: 4
    """

    type_: str = Field(
        default="PriceComponentTypeEnumeration", alias="@type", const=True
    )
