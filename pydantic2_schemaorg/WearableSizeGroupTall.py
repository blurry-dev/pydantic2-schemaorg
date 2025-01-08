from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.WearableSizeGroupEnumeration import (
    WearableSizeGroupEnumeration,
)


class WearableSizeGroupTall(WearableSizeGroupEnumeration):
    """Size group \"Tall\" for wearables.

    See: https://schema.org/WearableSizeGroupTall
    Model depth: 6
    """

    type_: str = Field(default="WearableSizeGroupTall", alias="@type", const=True)
