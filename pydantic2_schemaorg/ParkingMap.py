from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MapCategoryType import MapCategoryType


class ParkingMap(MapCategoryType):
    """A parking map.

    See: https://schema.org/ParkingMap
    Model depth: 5
    """

    type_: str = Field(default="ParkingMap", alias="@type", const=True)
