from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.PriceTypeEnumeration import PriceTypeEnumeration


class RegularPrice(PriceTypeEnumeration):
    """Represents the regular price (typically the previous advertised price before a sale) of an offered product.
     Often displayed as a strike-through price.

    See: https://schema.org/RegularPrice
    Model depth: 5
    """

    type_: str = Field(default="RegularPrice", alias="@type", const=True)
