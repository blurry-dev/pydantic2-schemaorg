from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.BodyOfWater import BodyOfWater


class Canal(BodyOfWater):
    """A canal, like the Panama Canal.

    See: https://schema.org/Canal
    Model depth: 5
    """

    type_: str = Field(default="Canal", alias="@type", const=True)
