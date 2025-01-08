from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Enumeration import Enumeration


class SizeSystemEnumeration(Enumeration):
    """Enumerates common size systems for different categories of products, for example \"EN-13402\" or \"UK\"
     for wearables or \"Imperial\" for screws.

    See: https://schema.org/SizeSystemEnumeration
    Model depth: 4
    """

    type_: str = Field(default="SizeSystemEnumeration", alias="@type", const=True)
