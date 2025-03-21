from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MusicReleaseFormatType import MusicReleaseFormatType


class CassetteFormat(MusicReleaseFormatType):
    """CassetteFormat.

    See: https://schema.org/CassetteFormat
    Model depth: 5
    """

    type_: str = Field(default="CassetteFormat", alias="@type", const=True)
