from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.WearableSizeSystemEnumeration import (
    WearableSizeSystemEnumeration,
)


class WearableSizeSystemAU(WearableSizeSystemEnumeration):
    """Australian size system for wearables.

    See: https://schema.org/WearableSizeSystemAU
    Model depth: 6
    """

    type_: str = Field(default="WearableSizeSystemAU", alias="@type", const=True)
