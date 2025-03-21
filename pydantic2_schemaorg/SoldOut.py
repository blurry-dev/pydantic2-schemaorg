from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.ItemAvailability import ItemAvailability


class SoldOut(ItemAvailability):
    """Indicates that the item has sold out.

    See: https://schema.org/SoldOut
    Model depth: 5
    """

    type_: str = Field(default="SoldOut", alias="@type", const=True)
