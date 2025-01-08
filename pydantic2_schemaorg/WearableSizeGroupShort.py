from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.WearableSizeGroupEnumeration import (
    WearableSizeGroupEnumeration,
)


class WearableSizeGroupShort(WearableSizeGroupEnumeration):
    """Size group \"Short\" for wearables.

    See: https://schema.org/WearableSizeGroupShort
    Model depth: 6
    """

    type_: str = Field(default="WearableSizeGroupShort", alias="@type", const=True)
