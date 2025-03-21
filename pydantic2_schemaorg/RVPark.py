from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.CivicStructure import CivicStructure


class RVPark(CivicStructure):
    """A place offering space for \"Recreational Vehicles\", Caravans, mobile homes and the like.

    See: https://schema.org/RVPark
    Model depth: 4
    """

    type_: str = Field(default="RVPark", alias="@type", const=True)
