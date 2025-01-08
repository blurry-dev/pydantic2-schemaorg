from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Landform import Landform


class BodyOfWater(Landform):
    """A body of water, such as a sea, ocean, or lake.

    See: https://schema.org/BodyOfWater
    Model depth: 4
    """

    type_: str = Field(default="BodyOfWater", alias="@type", const=True)
