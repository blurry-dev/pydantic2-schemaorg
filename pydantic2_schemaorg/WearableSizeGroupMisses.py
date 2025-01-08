from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.WearableSizeGroupEnumeration import (
    WearableSizeGroupEnumeration,
)


class WearableSizeGroupMisses(WearableSizeGroupEnumeration):
    """Size group \"Misses\" (also known as \"Missy\") for wearables.

    See: https://schema.org/WearableSizeGroupMisses
    Model depth: 6
    """

    type_: str = Field(default="WearableSizeGroupMisses", alias="@type", const=True)
