from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Event import Event


class ChildrensEvent(Event):
    """Event type: Children's event.

    See: https://schema.org/ChildrensEvent
    Model depth: 3
    """

    type_: str = Field(default="ChildrensEvent", alias="@type", const=True)
