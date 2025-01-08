from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Event import Event


class ComedyEvent(Event):
    """Event type: Comedy event.

    See: https://schema.org/ComedyEvent
    Model depth: 3
    """

    type_: str = Field(default="ComedyEvent", alias="@type", const=True)
