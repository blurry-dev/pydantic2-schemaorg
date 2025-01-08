from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.CivicStructure import CivicStructure


class BusStop(CivicStructure):
    """A bus stop.

    See: https://schema.org/BusStop
    Model depth: 4
    """

    type_: str = Field(default="BusStop", alias="@type", const=True)
