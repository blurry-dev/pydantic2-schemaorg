from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.PriceTypeEnumeration import PriceTypeEnumeration


class SalePrice(PriceTypeEnumeration):
    """Represents a sale price (usually active for a limited period) of an offered product.

    See: https://schema.org/SalePrice
    Model depth: 5
    """

    type_: str = Field(default="SalePrice", alias="@type", const=True)
