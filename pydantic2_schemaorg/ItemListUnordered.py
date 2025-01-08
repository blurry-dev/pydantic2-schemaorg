from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.ItemListOrderType import ItemListOrderType


class ItemListUnordered(ItemListOrderType):
    """An ItemList ordered with no explicit order.

    See: https://schema.org/ItemListUnordered
    Model depth: 5
    """

    type_: str = Field(default="ItemListUnordered", alias="@type", const=True)
