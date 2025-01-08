from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.IPTCDigitalSourceEnumeration import (
    IPTCDigitalSourceEnumeration,
)


class TrainedAlgorithmicMediaDigitalSource(IPTCDigitalSourceEnumeration):
    """Content coded as '<a href=\"https://cv.iptc.org/newscodes/digitalsourcetype/trainedAlgorithmicMedia\">trained
     algorithmic media</a>' using the IPTC <a href=\"https://cv.iptc.org/newscodes/digitalsourcetype/\">digital
     source type</a> vocabulary.

    See: https://schema.org/TrainedAlgorithmicMediaDigitalSource
    Model depth: 6
    """

    type_: str = Field(
        default="TrainedAlgorithmicMediaDigitalSource", alias="@type", const=True
    )
