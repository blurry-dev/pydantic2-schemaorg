from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.SportsActivityLocation import SportsActivityLocation


class SportsClub(SportsActivityLocation):
    """A sports club.

    See: https://schema.org/SportsClub
    Model depth: 5
    """

    type_: str = Field(default="SportsClub", alias="@type", const=True)
