from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Event import Event


class LiteraryEvent(Event):
    """Event type: Literary event.

    See: https://schema.org/LiteraryEvent
    Model depth: 3
    """

    type_: str = Field(default="LiteraryEvent", alias="@type", const=True)
