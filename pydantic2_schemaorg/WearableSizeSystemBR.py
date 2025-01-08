from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.WearableSizeSystemEnumeration import (
    WearableSizeSystemEnumeration,
)


class WearableSizeSystemBR(WearableSizeSystemEnumeration):
    """Brazilian size system for wearables.

    See: https://schema.org/WearableSizeSystemBR
    Model depth: 6
    """

    type_: str = Field(default="WearableSizeSystemBR", alias="@type", const=True)
