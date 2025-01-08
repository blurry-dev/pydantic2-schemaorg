from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Store import Store
from pydantic2_schemaorg.AutomotiveBusiness import AutomotiveBusiness


class AutoPartsStore(Store, AutomotiveBusiness):
    """An auto parts store.

    See: https://schema.org/AutoPartsStore
    Model depth: 5
    """

    type_: str = Field(default="AutoPartsStore", alias="@type", const=True)
