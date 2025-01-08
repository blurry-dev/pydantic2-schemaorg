from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.WearableSizeSystemEnumeration import (
    WearableSizeSystemEnumeration,
)


class WearableSizeSystemUS(WearableSizeSystemEnumeration):
    """United States size system for wearables.

    See: https://schema.org/WearableSizeSystemUS
    Model depth: 6
    """

    type_: str = Field(default="WearableSizeSystemUS", alias="@type", const=True)
