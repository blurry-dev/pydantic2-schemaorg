from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.WearableSizeGroupEnumeration import (
    WearableSizeGroupEnumeration,
)


class WearableSizeGroupBig(WearableSizeGroupEnumeration):
    """Size group \"Big\" for wearables.

    See: https://schema.org/WearableSizeGroupBig
    Model depth: 6
    """

    type_: str = Field(default="WearableSizeGroupBig", alias="@type", const=True)
