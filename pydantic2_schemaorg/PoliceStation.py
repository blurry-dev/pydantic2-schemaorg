from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.EmergencyService import EmergencyService
from pydantic2_schemaorg.CivicStructure import CivicStructure


class PoliceStation(EmergencyService, CivicStructure):
    """A police station.

    See: https://schema.org/PoliceStation
    Model depth: 4
    """

    type_: str = Field(default="PoliceStation", alias="@type", const=True)
