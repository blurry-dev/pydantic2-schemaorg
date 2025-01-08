from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.WearableSizeGroupEnumeration import (
    WearableSizeGroupEnumeration,
)


class WearableSizeGroupMaternity(WearableSizeGroupEnumeration):
    """Size group \"Maternity\" for wearables.

    See: https://schema.org/WearableSizeGroupMaternity
    Model depth: 6
    """

    type_: str = Field(default="WearableSizeGroupMaternity", alias="@type", const=True)
