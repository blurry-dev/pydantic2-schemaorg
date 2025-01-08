from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.SportsActivityLocation import SportsActivityLocation


class TennisComplex(SportsActivityLocation):
    """A tennis complex.

    See: https://schema.org/TennisComplex
    Model depth: 5
    """

    type_: str = Field(default="TennisComplex", alias="@type", const=True)
