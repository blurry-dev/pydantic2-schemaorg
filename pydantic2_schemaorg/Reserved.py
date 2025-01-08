from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.ItemAvailability import ItemAvailability


class Reserved(ItemAvailability):
    """Indicates that the item is reserved and therefore not available.

    See: https://schema.org/Reserved
    Model depth: 5
    """

    type_: str = Field(default="Reserved", alias="@type", const=True)
