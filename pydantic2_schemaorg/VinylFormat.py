from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MusicReleaseFormatType import MusicReleaseFormatType


class VinylFormat(MusicReleaseFormatType):
    """VinylFormat.

    See: https://schema.org/VinylFormat
    Model depth: 5
    """

    type_: str = Field(default="VinylFormat", alias="@type", const=True)
