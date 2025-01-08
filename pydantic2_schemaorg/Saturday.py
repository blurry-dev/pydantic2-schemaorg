from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.DayOfWeek import DayOfWeek


class Saturday(DayOfWeek):
    """The day of the week between Friday and Sunday.

    See: https://schema.org/Saturday
    Model depth: 5
    """

    type_: str = Field(default="Saturday", alias="@type", const=True)
