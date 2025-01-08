from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.StatusEnumeration import StatusEnumeration


class ReservationStatusType(StatusEnumeration):
    """Enumerated status values for Reservation.

    See: https://schema.org/ReservationStatusType
    Model depth: 5
    """

    type_: str = Field(default="ReservationStatusType", alias="@type", const=True)
