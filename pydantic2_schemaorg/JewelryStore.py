from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Store import Store


class JewelryStore(Store):
    """A jewelry store.

    See: https://schema.org/JewelryStore
    Model depth: 5
    """

    type_: str = Field(default="JewelryStore", alias="@type", const=True)
