from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Store import Store


class FurnitureStore(Store):
    """A furniture store.

    See: https://schema.org/FurnitureStore
    Model depth: 5
    """

    type_: str = Field(default="FurnitureStore", alias="@type", const=True)
