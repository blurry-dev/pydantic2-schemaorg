from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.WearableSizeSystemEnumeration import (
    WearableSizeSystemEnumeration,
)


class WearableSizeSystemEN13402(WearableSizeSystemEnumeration):
    """EN 13402 (joint European standard for size labelling of clothes).

    See: https://schema.org/WearableSizeSystemEN13402
    Model depth: 6
    """

    type_: str = Field(default="WearableSizeSystemEN13402", alias="@type", const=True)
