from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.PriceTypeEnumeration import PriceTypeEnumeration


class ListPrice(PriceTypeEnumeration):
    """Represents the list price of an offered product.

    See: https://schema.org/ListPrice
    Model depth: 5
    """

    type_: str = Field(default="ListPrice", alias="@type", const=True)
