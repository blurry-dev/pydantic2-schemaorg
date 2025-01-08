from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.GovernmentBuilding import GovernmentBuilding


class LegislativeBuilding(GovernmentBuilding):
    """A legislative building&#x2014;for example, the state capitol.

    See: https://schema.org/LegislativeBuilding
    Model depth: 5
    """

    type_: str = Field(default="LegislativeBuilding", alias="@type", const=True)
