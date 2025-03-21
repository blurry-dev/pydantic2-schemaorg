from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.SizeSystemEnumeration import SizeSystemEnumeration


class WearableSizeSystemEnumeration(SizeSystemEnumeration):
    """Enumerates common size systems specific for wearable products.

    See: https://schema.org/WearableSizeSystemEnumeration
    Model depth: 5
    """

    type_: str = Field(
        default="WearableSizeSystemEnumeration", alias="@type", const=True
    )
