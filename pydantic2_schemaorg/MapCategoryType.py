from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Enumeration import Enumeration


class MapCategoryType(Enumeration):
    """An enumeration of several kinds of Map.

    See: https://schema.org/MapCategoryType
    Model depth: 4
    """

    type_: str = Field(default="MapCategoryType", alias="@type", const=True)
