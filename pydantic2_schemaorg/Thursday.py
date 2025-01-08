from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.DayOfWeek import DayOfWeek


class Thursday(DayOfWeek):
    """The day of the week between Wednesday and Friday.

    See: https://schema.org/Thursday
    Model depth: 5
    """

    type_: str = Field(default="Thursday", alias="@type", const=True)
