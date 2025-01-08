from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.WearableSizeSystemEnumeration import (
    WearableSizeSystemEnumeration,
)


class WearableSizeSystemIT(WearableSizeSystemEnumeration):
    """Italian size system for wearables.

    See: https://schema.org/WearableSizeSystemIT
    Model depth: 6
    """

    type_: str = Field(default="WearableSizeSystemIT", alias="@type", const=True)
