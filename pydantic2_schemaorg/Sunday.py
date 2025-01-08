from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.DayOfWeek import DayOfWeek


class Sunday(DayOfWeek):
    """The day of the week between Saturday and Monday.

    See: https://schema.org/Sunday
    Model depth: 5
    """

    type_: str = Field(default="Sunday", alias="@type", const=True)
