from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.DayOfWeek import DayOfWeek


class Tuesday(DayOfWeek):
    """The day of the week between Monday and Wednesday.

    See: https://schema.org/Tuesday
    Model depth: 5
    """

    type_: str = Field(default="Tuesday", alias="@type", const=True)
