from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.PlaceOfWorship import PlaceOfWorship


class BuddhistTemple(PlaceOfWorship):
    """A Buddhist temple.

    See: https://schema.org/BuddhistTemple
    Model depth: 5
    """

    type_: str = Field(default="BuddhistTemple", alias="@type", const=True)
