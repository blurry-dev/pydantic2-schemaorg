from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.DayOfWeek import DayOfWeek


class Wednesday(DayOfWeek):
    """The day of the week between Tuesday and Thursday.

    See: https://schema.org/Wednesday
    Model depth: 5
    """

    type_: str = Field(default="Wednesday", alias="@type", const=True)
