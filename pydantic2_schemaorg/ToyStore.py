from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Store import Store


class ToyStore(Store):
    """A toy store.

    See: https://schema.org/ToyStore
    Model depth: 5
    """

    type_: str = Field(default="ToyStore", alias="@type", const=True)
