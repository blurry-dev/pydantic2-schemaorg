from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Store import Store


class ClothingStore(Store):
    """A clothing store.

    See: https://schema.org/ClothingStore
    Model depth: 5
    """

    type_: str = Field(default="ClothingStore", alias="@type", const=True)
