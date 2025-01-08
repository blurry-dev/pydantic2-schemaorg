from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Event import Event


class SaleEvent(Event):
    """Event type: Sales event.

    See: https://schema.org/SaleEvent
    Model depth: 3
    """

    type_: str = Field(default="SaleEvent", alias="@type", const=True)
