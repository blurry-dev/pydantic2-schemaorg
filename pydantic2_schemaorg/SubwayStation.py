from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.CivicStructure import CivicStructure


class SubwayStation(CivicStructure):
    """A subway station.

    See: https://schema.org/SubwayStation
    Model depth: 4
    """

    type_: str = Field(default="SubwayStation", alias="@type", const=True)
