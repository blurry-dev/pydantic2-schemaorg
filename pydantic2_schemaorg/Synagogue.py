from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.PlaceOfWorship import PlaceOfWorship


class Synagogue(PlaceOfWorship):
    """A synagogue.

    See: https://schema.org/Synagogue
    Model depth: 5
    """

    type_: str = Field(default="Synagogue", alias="@type", const=True)
