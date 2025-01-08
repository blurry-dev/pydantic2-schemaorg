from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic.v1 import Field
from pydantic2_schemaorg.CreativeWork import CreativeWork


class Map(CreativeWork):
    """A map.

    See: https://schema.org/Map
    Model depth: 3
    """

    type_: str = Field(default="Map", alias="@type", const=True)
    mapType: Optional[
        Union[List[Union["MapCategoryType", str]], "MapCategoryType", str]
    ] = Field(
        default=None,
        description="Indicates the kind of Map, from the MapCategoryType Enumeration.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.MapCategoryType import MapCategoryType
