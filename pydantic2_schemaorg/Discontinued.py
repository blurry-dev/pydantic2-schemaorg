from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.ItemAvailability import ItemAvailability


class Discontinued(ItemAvailability):
    """Indicates that the item has been discontinued.

    See: https://schema.org/Discontinued
    Model depth: 5
    """

    type_: str = Field(default="Discontinued", alias="@type", const=True)
