from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.EventAttendanceModeEnumeration import (
    EventAttendanceModeEnumeration,
)


class OfflineEventAttendanceMode(EventAttendanceModeEnumeration):
    """OfflineEventAttendanceMode - an event that is primarily conducted offline.

    See: https://schema.org/OfflineEventAttendanceMode
    Model depth: 5
    """

    type_: str = Field(default="OfflineEventAttendanceMode", alias="@type", const=True)
