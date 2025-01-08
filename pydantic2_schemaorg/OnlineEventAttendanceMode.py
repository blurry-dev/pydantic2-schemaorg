from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.EventAttendanceModeEnumeration import (
    EventAttendanceModeEnumeration,
)


class OnlineEventAttendanceMode(EventAttendanceModeEnumeration):
    """OnlineEventAttendanceMode - an event that is primarily conducted online.

    See: https://schema.org/OnlineEventAttendanceMode
    Model depth: 5
    """

    type_: str = Field(default="OnlineEventAttendanceMode", alias="@type", const=True)
