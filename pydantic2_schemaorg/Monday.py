from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.DayOfWeek import DayOfWeek


class Monday(DayOfWeek):
    """The day of the week between Sunday and Tuesday.

    See: https://schema.org/Monday
    Model depth: 5
    """

    type_: str = Field(default="Monday", alias="@type", const=True)
