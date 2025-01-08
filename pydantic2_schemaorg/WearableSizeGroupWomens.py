from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.WearableSizeGroupEnumeration import (
    WearableSizeGroupEnumeration,
)


class WearableSizeGroupWomens(WearableSizeGroupEnumeration):
    """Size group \"Womens\" for wearables.

    See: https://schema.org/WearableSizeGroupWomens
    Model depth: 6
    """

    type_: str = Field(default="WearableSizeGroupWomens", alias="@type", const=True)
