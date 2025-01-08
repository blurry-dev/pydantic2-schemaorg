from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Event import Event


class VisualArtsEvent(Event):
    """Event type: Visual arts event.

    See: https://schema.org/VisualArtsEvent
    Model depth: 3
    """

    type_: str = Field(default="VisualArtsEvent", alias="@type", const=True)
