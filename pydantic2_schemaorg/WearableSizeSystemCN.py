from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.WearableSizeSystemEnumeration import (
    WearableSizeSystemEnumeration,
)


class WearableSizeSystemCN(WearableSizeSystemEnumeration):
    """Chinese size system for wearables.

    See: https://schema.org/WearableSizeSystemCN
    Model depth: 6
    """

    type_: str = Field(default="WearableSizeSystemCN", alias="@type", const=True)
