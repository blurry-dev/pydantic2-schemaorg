from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.DigitalPlatformEnumeration import DigitalPlatformEnumeration


class AndroidPlatform(DigitalPlatformEnumeration):
    """Represents the broad notion of Android-based operating systems.

    See: https://schema.org/AndroidPlatform
    Model depth: 5
    """

    type_: str = Field(default="AndroidPlatform", alias="@type", const=True)
