from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Store import Store


class ShoeStore(Store):
    """A shoe store.

    See: https://schema.org/ShoeStore
    Model depth: 5
    """

    type_: str = Field(default="ShoeStore", alias="@type", const=True)
