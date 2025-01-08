from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Store import Store


class MensClothingStore(Store):
    """A men's clothing store.

    See: https://schema.org/MensClothingStore
    Model depth: 5
    """

    type_: str = Field(default="MensClothingStore", alias="@type", const=True)
