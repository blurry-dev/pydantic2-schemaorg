from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.EventAttendanceModeEnumeration import (
    EventAttendanceModeEnumeration,
)


class MixedEventAttendanceMode(EventAttendanceModeEnumeration):
    """MixedEventAttendanceMode - an event that is conducted as a combination of both offline and online modes.

    See: https://schema.org/MixedEventAttendanceMode
    Model depth: 5
    """

    type_: str = Field(default="MixedEventAttendanceMode", alias="@type", const=True)
