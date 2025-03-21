from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Store import Store


class ElectronicsStore(Store):
    """An electronics store.

    See: https://schema.org/ElectronicsStore
    Model depth: 5
    """

    type_: str = Field(default="ElectronicsStore", alias="@type", const=True)
