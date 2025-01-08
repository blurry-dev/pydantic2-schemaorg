from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Store import Store


class ComputerStore(Store):
    """A computer store.

    See: https://schema.org/ComputerStore
    Model depth: 5
    """

    type_: str = Field(default="ComputerStore", alias="@type", const=True)
