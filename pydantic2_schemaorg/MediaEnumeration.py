from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Enumeration import Enumeration


class MediaEnumeration(Enumeration):
    """MediaEnumeration enumerations are lists of codes, labels etc. useful for describing media objects. They
     may be reflections of externally developed lists, or created at schema.org, or a combination.

    See: https://schema.org/MediaEnumeration
    Model depth: 4
    """

    type_: str = Field(default="MediaEnumeration", alias="@type", const=True)
