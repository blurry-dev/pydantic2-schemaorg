from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.SportsActivityLocation import SportsActivityLocation
from pydantic2_schemaorg.CivicStructure import CivicStructure


class StadiumOrArena(SportsActivityLocation, CivicStructure):
    """A stadium.

    See: https://schema.org/StadiumOrArena
    Model depth: 4
    """

    type_: str = Field(default="StadiumOrArena", alias="@type", const=True)
