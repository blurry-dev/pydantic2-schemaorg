from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Store import Store


class SportingGoodsStore(Store):
    """A sporting goods store.

    See: https://schema.org/SportingGoodsStore
    Model depth: 5
    """

    type_: str = Field(default="SportingGoodsStore", alias="@type", const=True)
