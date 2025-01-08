from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.CivicStructure import CivicStructure


class BusStation(CivicStructure):
    """A bus station.

    See: https://schema.org/BusStation
    Model depth: 4
    """

    type_: str = Field(default="BusStation", alias="@type", const=True)
