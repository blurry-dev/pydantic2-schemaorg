from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MapCategoryType import MapCategoryType


class SeatingMap(MapCategoryType):
    """A seating map.

    See: https://schema.org/SeatingMap
    Model depth: 5
    """

    type_: str = Field(default="SeatingMap", alias="@type", const=True)
