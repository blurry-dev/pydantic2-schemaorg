from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MusicReleaseFormatType import MusicReleaseFormatType


class DigitalAudioTapeFormat(MusicReleaseFormatType):
    """DigitalAudioTapeFormat.

    See: https://schema.org/DigitalAudioTapeFormat
    Model depth: 5
    """

    type_: str = Field(default="DigitalAudioTapeFormat", alias="@type", const=True)
