from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.ItemListOrderType import ItemListOrderType


class ItemListOrderAscending(ItemListOrderType):
    """An ItemList ordered with lower values listed first.

    See: https://schema.org/ItemListOrderAscending
    Model depth: 5
    """

    type_: str = Field(default="ItemListOrderAscending", alias="@type", const=True)
