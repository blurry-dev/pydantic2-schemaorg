from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.WearableSizeSystemEnumeration import (
    WearableSizeSystemEnumeration,
)


class WearableSizeSystemFR(WearableSizeSystemEnumeration):
    """French size system for wearables.

    See: https://schema.org/WearableSizeSystemFR
    Model depth: 6
    """

    type_: str = Field(default="WearableSizeSystemFR", alias="@type", const=True)
