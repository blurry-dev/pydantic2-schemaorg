from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.PerformingGroup import PerformingGroup


class DanceGroup(PerformingGroup):
    """A dance group&#x2014;for example, the Alvin Ailey Dance Theater or Riverdance.

    See: https://schema.org/DanceGroup
    Model depth: 4
    """

    type_: str = Field(default="DanceGroup", alias="@type", const=True)
