from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.WearableSizeGroupEnumeration import (
    WearableSizeGroupEnumeration,
)


class WearableSizeGroupJuniors(WearableSizeGroupEnumeration):
    """Size group \"Juniors\" for wearables.

    See: https://schema.org/WearableSizeGroupJuniors
    Model depth: 6
    """

    type_: str = Field(default="WearableSizeGroupJuniors", alias="@type", const=True)
