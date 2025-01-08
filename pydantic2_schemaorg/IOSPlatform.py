from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.DigitalPlatformEnumeration import DigitalPlatformEnumeration


class IOSPlatform(DigitalPlatformEnumeration):
    """Represents the broad notion of iOS-based operating systems.

    See: https://schema.org/IOSPlatform
    Model depth: 5
    """

    type_: str = Field(default="IOSPlatform", alias="@type", const=True)
