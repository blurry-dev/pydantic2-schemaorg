from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.BodyOfWater import BodyOfWater


class Reservoir(BodyOfWater):
    """A reservoir of water, typically an artificially created lake, like the Lake Kariba reservoir.

    See: https://schema.org/Reservoir
    Model depth: 5
    """

    type_: str = Field(default="Reservoir", alias="@type", const=True)
