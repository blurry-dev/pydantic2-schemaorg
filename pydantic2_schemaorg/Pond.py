from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.BodyOfWater import BodyOfWater


class Pond(BodyOfWater):
    """A pond.

    See: https://schema.org/Pond
    Model depth: 5
    """

    type_: str = Field(default="Pond", alias="@type", const=True)
