from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.BroadcastChannel import BroadcastChannel


class TelevisionChannel(BroadcastChannel):
    """A unique instance of a television BroadcastService on a CableOrSatelliteService lineup.

    See: https://schema.org/TelevisionChannel
    Model depth: 4
    """

    type_: str = Field(default="TelevisionChannel", alias="@type", const=True)
