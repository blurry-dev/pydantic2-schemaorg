from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Store import Store


class PetStore(Store):
    """A pet store.

    See: https://schema.org/PetStore
    Model depth: 5
    """

    type_: str = Field(default="PetStore", alias="@type", const=True)
