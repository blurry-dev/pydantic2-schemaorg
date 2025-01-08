from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.DigitalPlatformEnumeration import DigitalPlatformEnumeration


class GenericWebPlatform(DigitalPlatformEnumeration):
    """Represents the generic notion of the Web Platform. More specific codes include [[MobileWebPlatform]] and
     [[DesktopWebPlatform]], as an incomplete list.

    See: https://schema.org/GenericWebPlatform
    Model depth: 5
    """

    type_: str = Field(default="GenericWebPlatform", alias="@type", const=True)
