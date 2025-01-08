from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.WearableSizeGroupEnumeration import (
    WearableSizeGroupEnumeration,
)


class WearableSizeGroupMens(WearableSizeGroupEnumeration):
    """Size group \"Mens\" for wearables.

    See: https://schema.org/WearableSizeGroupMens
    Model depth: 6
    """

    type_: str = Field(default="WearableSizeGroupMens", alias="@type", const=True)
