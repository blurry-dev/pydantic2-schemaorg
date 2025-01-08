from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Store import Store


class GardenStore(Store):
    """A garden store.

    See: https://schema.org/GardenStore
    Model depth: 5
    """

    type_: str = Field(default="GardenStore", alias="@type", const=True)
