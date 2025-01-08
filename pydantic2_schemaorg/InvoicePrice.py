from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.PriceTypeEnumeration import PriceTypeEnumeration


class InvoicePrice(PriceTypeEnumeration):
    """Represents the invoice price of an offered product.

    See: https://schema.org/InvoicePrice
    Model depth: 5
    """

    type_: str = Field(default="InvoicePrice", alias="@type", const=True)
