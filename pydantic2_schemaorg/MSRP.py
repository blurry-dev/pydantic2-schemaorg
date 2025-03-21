from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.PriceTypeEnumeration import PriceTypeEnumeration


class MSRP(PriceTypeEnumeration):
    """Represents the manufacturer suggested retail price (\"MSRP\") of an offered product.

    See: https://schema.org/MSRP
    Model depth: 5
    """

    type_: str = Field(default="MSRP", alias="@type", const=True)
