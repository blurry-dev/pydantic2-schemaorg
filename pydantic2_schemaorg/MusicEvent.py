from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Event import Event


class MusicEvent(Event):
    """Event type: Music event.

    See: https://schema.org/MusicEvent
    Model depth: 3
    """

    type_: str = Field(default="MusicEvent", alias="@type", const=True)
