from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Store import Store


class HardwareStore(Store):
    """A hardware store.

    See: https://schema.org/HardwareStore
    Model depth: 5
    """

    type_: str = Field(default="HardwareStore", alias="@type", const=True)
