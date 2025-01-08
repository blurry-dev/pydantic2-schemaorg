from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Event import Event


class BusinessEvent(Event):
    """Event type: Business event.

    See: https://schema.org/BusinessEvent
    Model depth: 3
    """

    type_: str = Field(default="BusinessEvent", alias="@type", const=True)
