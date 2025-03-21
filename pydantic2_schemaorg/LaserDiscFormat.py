from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MusicReleaseFormatType import MusicReleaseFormatType


class LaserDiscFormat(MusicReleaseFormatType):
    """LaserDiscFormat.

    See: https://schema.org/LaserDiscFormat
    Model depth: 5
    """

    type_: str = Field(default="LaserDiscFormat", alias="@type", const=True)
