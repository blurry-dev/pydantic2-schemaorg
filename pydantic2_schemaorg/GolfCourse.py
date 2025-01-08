from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.SportsActivityLocation import SportsActivityLocation


class GolfCourse(SportsActivityLocation):
    """A golf course.

    See: https://schema.org/GolfCourse
    Model depth: 5
    """

    type_: str = Field(default="GolfCourse", alias="@type", const=True)
