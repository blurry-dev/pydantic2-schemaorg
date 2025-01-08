from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.AutomotiveBusiness import AutomotiveBusiness


class GasStation(AutomotiveBusiness):
    """A gas station.

    See: https://schema.org/GasStation
    Model depth: 5
    """

    type_: str = Field(default="GasStation", alias="@type", const=True)
