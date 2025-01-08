from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.PlaceOfWorship import PlaceOfWorship


class HinduTemple(PlaceOfWorship):
    """A Hindu temple.

    See: https://schema.org/HinduTemple
    Model depth: 5
    """

    type_: str = Field(default="HinduTemple", alias="@type", const=True)
