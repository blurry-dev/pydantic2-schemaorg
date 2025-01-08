from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Resort import Resort
from pydantic2_schemaorg.SportsActivityLocation import SportsActivityLocation


class SkiResort(Resort, SportsActivityLocation):
    """A ski resort.

    See: https://schema.org/SkiResort
    Model depth: 5
    """

    type_: str = Field(default="SkiResort", alias="@type", const=True)
