from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.DigitalPlatformEnumeration import DigitalPlatformEnumeration


class DesktopWebPlatform(DigitalPlatformEnumeration):
    """Represents the broad notion of 'desktop' browsers as a Web Platform.

    See: https://schema.org/DesktopWebPlatform
    Model depth: 5
    """

    type_: str = Field(default="DesktopWebPlatform", alias="@type", const=True)
