from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.WearableSizeGroupEnumeration import (
    WearableSizeGroupEnumeration,
)


class WearableSizeGroupExtraShort(WearableSizeGroupEnumeration):
    """Size group \"Extra Short\" for wearables.

    See: https://schema.org/WearableSizeGroupExtraShort
    Model depth: 6
    """

    type_: str = Field(default="WearableSizeGroupExtraShort", alias="@type", const=True)
