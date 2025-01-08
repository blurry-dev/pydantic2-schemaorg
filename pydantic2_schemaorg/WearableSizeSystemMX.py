from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.WearableSizeSystemEnumeration import (
    WearableSizeSystemEnumeration,
)


class WearableSizeSystemMX(WearableSizeSystemEnumeration):
    """Mexican size system for wearables.

    See: https://schema.org/WearableSizeSystemMX
    Model depth: 6
    """

    type_: str = Field(default="WearableSizeSystemMX", alias="@type", const=True)
