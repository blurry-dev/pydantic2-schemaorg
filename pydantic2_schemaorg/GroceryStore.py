from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Store import Store


class GroceryStore(Store):
    """A grocery store.

    See: https://schema.org/GroceryStore
    Model depth: 5
    """

    type_: str = Field(default="GroceryStore", alias="@type", const=True)
