from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.PriceTypeEnumeration import PriceTypeEnumeration


class SRP(PriceTypeEnumeration):
    """Represents the suggested retail price (\"SRP\") of an offered product.

    See: https://schema.org/SRP
    Model depth: 5
    """

    type_: str = Field(default="SRP", alias="@type", const=True)
