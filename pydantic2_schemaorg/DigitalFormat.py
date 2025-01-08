from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MusicReleaseFormatType import MusicReleaseFormatType


class DigitalFormat(MusicReleaseFormatType):
    """DigitalFormat.

    See: https://schema.org/DigitalFormat
    Model depth: 5
    """

    type_: str = Field(default="DigitalFormat", alias="@type", const=True)
