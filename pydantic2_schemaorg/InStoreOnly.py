from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.ItemAvailability import ItemAvailability


class InStoreOnly(ItemAvailability):
    """Indicates that the item is available only at physical locations.

    See: https://schema.org/InStoreOnly
    Model depth: 5
    """

    type_: str = Field(default="InStoreOnly", alias="@type", const=True)
