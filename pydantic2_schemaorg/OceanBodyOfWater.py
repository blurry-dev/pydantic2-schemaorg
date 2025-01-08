from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.BodyOfWater import BodyOfWater


class OceanBodyOfWater(BodyOfWater):
    """An ocean (for example, the Pacific).

    See: https://schema.org/OceanBodyOfWater
    Model depth: 5
    """

    type_: str = Field(default="OceanBodyOfWater", alias="@type", const=True)
