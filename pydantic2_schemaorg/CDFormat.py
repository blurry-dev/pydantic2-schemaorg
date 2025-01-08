from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MusicReleaseFormatType import MusicReleaseFormatType


class CDFormat(MusicReleaseFormatType):
    """CDFormat.

    See: https://schema.org/CDFormat
    Model depth: 5
    """

    type_: str = Field(default="CDFormat", alias="@type", const=True)
