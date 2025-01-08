from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic.v1 import Field
from pydantic2_schemaorg.Place import Place


class Residence(Place):
    """The place where a person lives.

    See: https://schema.org/Residence
    Model depth: 3
    """

    type_: str = Field(default="Residence", alias="@type", const=True)
    accommodationFloorPlan: Optional[
        Union[List[Union["FloorPlan", str]], "FloorPlan", str]
    ] = Field(
        default=None,
        description="A floorplan of some [[Accommodation]].",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.FloorPlan import FloorPlan
