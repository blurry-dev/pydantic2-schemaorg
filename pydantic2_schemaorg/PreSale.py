from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.ItemAvailability import ItemAvailability


class PreSale(ItemAvailability):
    """Indicates that the item is available for ordering and delivery before general availability.

    See: https://schema.org/PreSale
    Model depth: 5
    """

    type_: str = Field(default="PreSale", alias="@type", const=True)
