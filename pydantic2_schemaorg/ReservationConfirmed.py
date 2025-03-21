from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.ReservationStatusType import ReservationStatusType


class ReservationConfirmed(ReservationStatusType):
    """The status of a confirmed reservation.

    See: https://schema.org/ReservationConfirmed
    Model depth: 6
    """

    type_: str = Field(default="ReservationConfirmed", alias="@type", const=True)
