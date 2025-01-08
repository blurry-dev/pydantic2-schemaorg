from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.IPTCDigitalSourceEnumeration import (
    IPTCDigitalSourceEnumeration,
)


class VirtualRecordingDigitalSource(IPTCDigitalSourceEnumeration):
    """Content coded as '<a href=\"https://cv.iptc.org/newscodes/digitalsourcetype/virtualRecording\">virtual
     recording</a>' using the IPTC <a href=\"https://cv.iptc.org/newscodes/digitalsourcetype/\">digital
     source type</a> vocabulary.

    See: https://schema.org/VirtualRecordingDigitalSource
    Model depth: 6
    """

    type_: str = Field(
        default="VirtualRecordingDigitalSource", alias="@type", const=True
    )
