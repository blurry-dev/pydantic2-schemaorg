from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.LocalBusiness import LocalBusiness


class Store(LocalBusiness):
    """A retail good store.

    See: https://schema.org/Store
    Model depth: 4
    """

    type_: str = Field(default="Store", alias="@type", const=True)
