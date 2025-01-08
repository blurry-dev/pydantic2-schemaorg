from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.GovernmentBuilding import GovernmentBuilding


class CityHall(GovernmentBuilding):
    """A city hall.

    See: https://schema.org/CityHall
    Model depth: 5
    """

    type_: str = Field(default="CityHall", alias="@type", const=True)
