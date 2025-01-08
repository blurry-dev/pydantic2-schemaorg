from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.BodyOfWater import BodyOfWater


class LakeBodyOfWater(BodyOfWater):
    """A lake (for example, Lake Pontrachain).

    See: https://schema.org/LakeBodyOfWater
    Model depth: 5
    """

    type_: str = Field(default="LakeBodyOfWater", alias="@type", const=True)
