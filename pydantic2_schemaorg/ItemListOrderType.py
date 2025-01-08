from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Enumeration import Enumeration


class ItemListOrderType(Enumeration):
    """Enumerated for values for itemListOrder for indicating how an ordered ItemList is organized.

    See: https://schema.org/ItemListOrderType
    Model depth: 4
    """

    type_: str = Field(default="ItemListOrderType", alias="@type", const=True)
