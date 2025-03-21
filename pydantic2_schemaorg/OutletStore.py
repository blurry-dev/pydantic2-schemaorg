from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Store import Store


class OutletStore(Store):
    """An outlet store.

    See: https://schema.org/OutletStore
    Model depth: 5
    """

    type_: str = Field(default="OutletStore", alias="@type", const=True)
