from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.SportsActivityLocation import SportsActivityLocation


class BowlingAlley(SportsActivityLocation):
    """A bowling alley.

    See: https://schema.org/BowlingAlley
    Model depth: 5
    """

    type_: str = Field(default="BowlingAlley", alias="@type", const=True)
