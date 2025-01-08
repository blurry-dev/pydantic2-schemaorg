from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.WearableSizeGroupEnumeration import (
    WearableSizeGroupEnumeration,
)


class WearableSizeGroupBoys(WearableSizeGroupEnumeration):
    """Size group \"Boys\" for wearables.

    See: https://schema.org/WearableSizeGroupBoys
    Model depth: 6
    """

    type_: str = Field(default="WearableSizeGroupBoys", alias="@type", const=True)
