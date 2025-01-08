from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.ItemListOrderType import ItemListOrderType


class ItemListOrderDescending(ItemListOrderType):
    """An ItemList ordered with higher values listed first.

    See: https://schema.org/ItemListOrderDescending
    Model depth: 5
    """

    type_: str = Field(default="ItemListOrderDescending", alias="@type", const=True)
