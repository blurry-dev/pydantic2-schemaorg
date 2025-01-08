from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.SizeGroupEnumeration import SizeGroupEnumeration


class WearableSizeGroupEnumeration(SizeGroupEnumeration):
    """Enumerates common size groups (also known as \"size types\") for wearable products.

    See: https://schema.org/WearableSizeGroupEnumeration
    Model depth: 5
    """

    type_: str = Field(
        default="WearableSizeGroupEnumeration", alias="@type", const=True
    )
