from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Event import Event


class DanceEvent(Event):
    """Event type: A social dance.

    See: https://schema.org/DanceEvent
    Model depth: 3
    """

    type_: str = Field(default="DanceEvent", alias="@type", const=True)
