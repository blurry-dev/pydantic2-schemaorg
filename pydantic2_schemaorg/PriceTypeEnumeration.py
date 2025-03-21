from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Enumeration import Enumeration


class PriceTypeEnumeration(Enumeration):
    """Enumerates different price types, for example list price, invoice price, and sale price.

    See: https://schema.org/PriceTypeEnumeration
    Model depth: 4
    """

    type_: str = Field(default="PriceTypeEnumeration", alias="@type", const=True)
