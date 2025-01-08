from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.ItemAvailability import ItemAvailability


class InStock(ItemAvailability):
    """Indicates that the item is in stock.

    See: https://schema.org/InStock
    Model depth: 5
    """

    type_: str = Field(default="InStock", alias="@type", const=True)
