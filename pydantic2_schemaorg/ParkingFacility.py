from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.CivicStructure import CivicStructure


class ParkingFacility(CivicStructure):
    """A parking lot or other parking facility.

    See: https://schema.org/ParkingFacility
    Model depth: 4
    """

    type_: str = Field(default="ParkingFacility", alias="@type", const=True)
