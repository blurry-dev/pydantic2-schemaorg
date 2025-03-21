from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.WearableSizeSystemEnumeration import (
    WearableSizeSystemEnumeration,
)


class WearableSizeSystemContinental(WearableSizeSystemEnumeration):
    """Continental size system for wearables.

    See: https://schema.org/WearableSizeSystemContinental
    Model depth: 6
    """

    type_: str = Field(
        default="WearableSizeSystemContinental", alias="@type", const=True
    )
