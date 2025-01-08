from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.WearableSizeSystemEnumeration import (
    WearableSizeSystemEnumeration,
)


class WearableSizeSystemJP(WearableSizeSystemEnumeration):
    """Japanese size system for wearables.

    See: https://schema.org/WearableSizeSystemJP
    Model depth: 6
    """

    type_: str = Field(default="WearableSizeSystemJP", alias="@type", const=True)
