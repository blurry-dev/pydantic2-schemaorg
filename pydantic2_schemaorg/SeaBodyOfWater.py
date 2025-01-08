from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.BodyOfWater import BodyOfWater


class SeaBodyOfWater(BodyOfWater):
    """A sea (for example, the Caspian sea).

    See: https://schema.org/SeaBodyOfWater
    Model depth: 5
    """

    type_: str = Field(default="SeaBodyOfWater", alias="@type", const=True)
