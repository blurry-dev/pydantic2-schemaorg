from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.WearableSizeGroupEnumeration import (
    WearableSizeGroupEnumeration,
)


class WearableSizeGroupPlus(WearableSizeGroupEnumeration):
    """Size group \"Plus\" for wearables.

    See: https://schema.org/WearableSizeGroupPlus
    Model depth: 6
    """

    type_: str = Field(default="WearableSizeGroupPlus", alias="@type", const=True)
