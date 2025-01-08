from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.WearableSizeSystemEnumeration import (
    WearableSizeSystemEnumeration,
)


class WearableSizeSystemUK(WearableSizeSystemEnumeration):
    """United Kingdom size system for wearables.

    See: https://schema.org/WearableSizeSystemUK
    Model depth: 6
    """

    type_: str = Field(default="WearableSizeSystemUK", alias="@type", const=True)
