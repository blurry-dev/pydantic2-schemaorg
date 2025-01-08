from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Place import Place


class LandmarksOrHistoricalBuildings(Place):
    """An historical landmark or building.

    See: https://schema.org/LandmarksOrHistoricalBuildings
    Model depth: 3
    """

    type_: str = Field(
        default="LandmarksOrHistoricalBuildings", alias="@type", const=True
    )
