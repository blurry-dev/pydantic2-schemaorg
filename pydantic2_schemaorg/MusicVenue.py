from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.CivicStructure import CivicStructure


class MusicVenue(CivicStructure):
    """A music venue.

    See: https://schema.org/MusicVenue
    Model depth: 4
    """

    type_: str = Field(default="MusicVenue", alias="@type", const=True)
