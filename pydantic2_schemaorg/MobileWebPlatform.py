from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.DigitalPlatformEnumeration import DigitalPlatformEnumeration


class MobileWebPlatform(DigitalPlatformEnumeration):
    """Represents the broad notion of 'mobile' browsers as a Web Platform.

    See: https://schema.org/MobileWebPlatform
    Model depth: 5
    """

    type_: str = Field(default="MobileWebPlatform", alias="@type", const=True)
