from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.WearableSizeSystemEnumeration import (
    WearableSizeSystemEnumeration,
)


class WearableSizeSystemDE(WearableSizeSystemEnumeration):
    """German size system for wearables.

    See: https://schema.org/WearableSizeSystemDE
    Model depth: 6
    """

    type_: str = Field(default="WearableSizeSystemDE", alias="@type", const=True)
