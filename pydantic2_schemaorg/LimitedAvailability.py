from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.ItemAvailability import ItemAvailability


class LimitedAvailability(ItemAvailability):
    """Indicates that the item has limited availability.

    See: https://schema.org/LimitedAvailability
    Model depth: 5
    """

    type_: str = Field(default="LimitedAvailability", alias="@type", const=True)
