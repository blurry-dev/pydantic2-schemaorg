from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.ItemAvailability import ItemAvailability


class MadeToOrder(ItemAvailability):
    """Indicates that the item is made to order (custom made).

    See: https://schema.org/MadeToOrder
    Model depth: 5
    """

    type_: str = Field(default="MadeToOrder", alias="@type", const=True)
