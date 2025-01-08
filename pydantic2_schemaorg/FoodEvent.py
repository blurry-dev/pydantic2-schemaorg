from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Event import Event


class FoodEvent(Event):
    """Event type: Food event.

    See: https://schema.org/FoodEvent
    Model depth: 3
    """

    type_: str = Field(default="FoodEvent", alias="@type", const=True)
