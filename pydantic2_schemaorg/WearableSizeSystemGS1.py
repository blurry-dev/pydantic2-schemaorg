from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.WearableSizeSystemEnumeration import (
    WearableSizeSystemEnumeration,
)


class WearableSizeSystemGS1(WearableSizeSystemEnumeration):
    """GS1 (formerly NRF) size system for wearables.

    See: https://schema.org/WearableSizeSystemGS1
    Model depth: 6
    """

    type_: str = Field(default="WearableSizeSystemGS1", alias="@type", const=True)
