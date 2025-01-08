from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.PlaceOfWorship import PlaceOfWorship


class Mosque(PlaceOfWorship):
    """A mosque.

    See: https://schema.org/Mosque
    Model depth: 5
    """

    type_: str = Field(default="Mosque", alias="@type", const=True)
