from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.ItemAvailability import ItemAvailability


class PreOrder(ItemAvailability):
    """Indicates that the item is available for pre-order.

    See: https://schema.org/PreOrder
    Model depth: 5
    """

    type_: str = Field(default="PreOrder", alias="@type", const=True)
