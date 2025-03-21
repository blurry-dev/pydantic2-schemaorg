from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MusicReleaseFormatType import MusicReleaseFormatType


class DVDFormat(MusicReleaseFormatType):
    """DVDFormat.

    See: https://schema.org/DVDFormat
    Model depth: 5
    """

    type_: str = Field(default="DVDFormat", alias="@type", const=True)
