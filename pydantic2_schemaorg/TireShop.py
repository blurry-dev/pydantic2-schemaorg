from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Store import Store


class TireShop(Store):
    """A tire shop.

    See: https://schema.org/TireShop
    Model depth: 5
    """

    type_: str = Field(default="TireShop", alias="@type", const=True)
