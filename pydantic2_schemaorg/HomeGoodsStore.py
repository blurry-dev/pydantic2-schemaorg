from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Store import Store


class HomeGoodsStore(Store):
    """A home goods store.

    See: https://schema.org/HomeGoodsStore
    Model depth: 5
    """

    type_: str = Field(default="HomeGoodsStore", alias="@type", const=True)
