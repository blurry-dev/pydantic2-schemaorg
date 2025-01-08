from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.CivicStructure import CivicStructure


class GovernmentBuilding(CivicStructure):
    """A government building.

    See: https://schema.org/GovernmentBuilding
    Model depth: 4
    """

    type_: str = Field(default="GovernmentBuilding", alias="@type", const=True)
