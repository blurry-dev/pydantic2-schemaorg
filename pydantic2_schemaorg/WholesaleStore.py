from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Store import Store


class WholesaleStore(Store):
    """A wholesale store.

    See: https://schema.org/WholesaleStore
    Model depth: 5
    """

    type_: str = Field(default="WholesaleStore", alias="@type", const=True)
