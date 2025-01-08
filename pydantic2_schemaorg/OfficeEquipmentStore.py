from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Store import Store


class OfficeEquipmentStore(Store):
    """An office equipment store.

    See: https://schema.org/OfficeEquipmentStore
    Model depth: 5
    """

    type_: str = Field(default="OfficeEquipmentStore", alias="@type", const=True)
