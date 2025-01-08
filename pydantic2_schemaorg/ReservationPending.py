from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.ReservationStatusType import ReservationStatusType


class ReservationPending(ReservationStatusType):
    """The status of a reservation when a request has been sent, but not confirmed.

    See: https://schema.org/ReservationPending
    Model depth: 6
    """

    type_: str = Field(default="ReservationPending", alias="@type", const=True)
