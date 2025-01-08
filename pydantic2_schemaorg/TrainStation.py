from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.CivicStructure import CivicStructure


class TrainStation(CivicStructure):
    """A train station.

    See: https://schema.org/TrainStation
    Model depth: 4
    """

    type_: str = Field(default="TrainStation", alias="@type", const=True)
