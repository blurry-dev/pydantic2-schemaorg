from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Enumeration import Enumeration


class DigitalPlatformEnumeration(Enumeration):
    """Enumerates some common technology platforms, for use with properties such as [[actionPlatform]]. It is
     not supposed to be comprehensive - when a suitable code is not enumerated here, textual or URL values can be
     used instead. These codes are at a fairly high level and do not deal with versioning and other nuance. Additional
     codes can be suggested [in github](https://github.com/schemaorg/schemaorg/issues/3057).

    See: https://schema.org/DigitalPlatformEnumeration
    Model depth: 4
    """

    type_: str = Field(default="DigitalPlatformEnumeration", alias="@type", const=True)
