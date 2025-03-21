from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.WearableSizeGroupEnumeration import (
    WearableSizeGroupEnumeration,
)


class WearableSizeGroupHusky(WearableSizeGroupEnumeration):
    """Size group \"Husky\" (or \"Stocky\") for wearables.

    See: https://schema.org/WearableSizeGroupHusky
    Model depth: 6
    """

    type_: str = Field(default="WearableSizeGroupHusky", alias="@type", const=True)
