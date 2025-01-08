from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.WearableSizeGroupEnumeration import (
    WearableSizeGroupEnumeration,
)


class WearableSizeGroupPetite(WearableSizeGroupEnumeration):
    """Size group \"Petite\" for wearables.

    See: https://schema.org/WearableSizeGroupPetite
    Model depth: 6
    """

    type_: str = Field(default="WearableSizeGroupPetite", alias="@type", const=True)
