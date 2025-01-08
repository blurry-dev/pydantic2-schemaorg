from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.WearableSizeGroupEnumeration import (
    WearableSizeGroupEnumeration,
)


class WearableSizeGroupInfants(WearableSizeGroupEnumeration):
    """Size group \"Infants\" for wearables.

    See: https://schema.org/WearableSizeGroupInfants
    Model depth: 6
    """

    type_: str = Field(default="WearableSizeGroupInfants", alias="@type", const=True)
