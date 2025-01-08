from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.WearableSizeSystemEnumeration import (
    WearableSizeSystemEnumeration,
)


class WearableSizeSystemEurope(WearableSizeSystemEnumeration):
    """European size system for wearables.

    See: https://schema.org/WearableSizeSystemEurope
    Model depth: 6
    """

    type_: str = Field(default="WearableSizeSystemEurope", alias="@type", const=True)
