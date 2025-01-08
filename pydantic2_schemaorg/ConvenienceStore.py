from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Store import Store


class ConvenienceStore(Store):
    """A convenience store.

    See: https://schema.org/ConvenienceStore
    Model depth: 5
    """

    type_: str = Field(default="ConvenienceStore", alias="@type", const=True)
