from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.WearableSizeGroupEnumeration import (
    WearableSizeGroupEnumeration,
)


class WearableSizeGroupRegular(WearableSizeGroupEnumeration):
    """Size group \"Regular\" for wearables.

    See: https://schema.org/WearableSizeGroupRegular
    Model depth: 6
    """

    type_: str = Field(default="WearableSizeGroupRegular", alias="@type", const=True)
