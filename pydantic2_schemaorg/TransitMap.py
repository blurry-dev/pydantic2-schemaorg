from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MapCategoryType import MapCategoryType


class TransitMap(MapCategoryType):
    """A transit map.

    See: https://schema.org/TransitMap
    Model depth: 5
    """

    type_: str = Field(default="TransitMap", alias="@type", const=True)
