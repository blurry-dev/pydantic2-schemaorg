from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.SportsActivityLocation import SportsActivityLocation


class ExerciseGym(SportsActivityLocation):
    """A gym.

    See: https://schema.org/ExerciseGym
    Model depth: 5
    """

    type_: str = Field(default="ExerciseGym", alias="@type", const=True)
