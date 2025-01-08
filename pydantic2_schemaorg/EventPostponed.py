from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.EventStatusType import EventStatusType


class EventPostponed(EventStatusType):
    """The event has been postponed and no new date has been set. The event's previousStartDate should be set.

    See: https://schema.org/EventPostponed
    Model depth: 6
    """

    type_: str = Field(default="EventPostponed", alias="@type", const=True)
