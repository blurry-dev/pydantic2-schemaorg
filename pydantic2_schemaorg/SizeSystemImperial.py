from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.SizeSystemEnumeration import SizeSystemEnumeration


class SizeSystemImperial(SizeSystemEnumeration):
    """Imperial size system.

    See: https://schema.org/SizeSystemImperial
    Model depth: 5
    """

    type_: str = Field(default="SizeSystemImperial", alias="@type", const=True)
