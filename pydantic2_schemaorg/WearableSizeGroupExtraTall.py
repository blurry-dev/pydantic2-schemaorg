from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.WearableSizeGroupEnumeration import (
    WearableSizeGroupEnumeration,
)


class WearableSizeGroupExtraTall(WearableSizeGroupEnumeration):
    """Size group \"Extra Tall\" for wearables.

    See: https://schema.org/WearableSizeGroupExtraTall
    Model depth: 6
    """

    type_: str = Field(default="WearableSizeGroupExtraTall", alias="@type", const=True)
