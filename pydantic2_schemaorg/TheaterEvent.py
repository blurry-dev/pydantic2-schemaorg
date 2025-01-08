from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Event import Event


class TheaterEvent(Event):
    """Event type: Theater performance.

    See: https://schema.org/TheaterEvent
    Model depth: 3
    """

    type_: str = Field(default="TheaterEvent", alias="@type", const=True)
