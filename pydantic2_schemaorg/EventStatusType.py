from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.StatusEnumeration import StatusEnumeration


class EventStatusType(StatusEnumeration):
    """EventStatusType is an enumeration type whose instances represent several states that an Event may be in.

    See: https://schema.org/EventStatusType
    Model depth: 5
    """

    type_: str = Field(default="EventStatusType", alias="@type", const=True)
