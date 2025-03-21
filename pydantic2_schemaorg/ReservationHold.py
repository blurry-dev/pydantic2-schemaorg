from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.ReservationStatusType import ReservationStatusType


class ReservationHold(ReservationStatusType):
    """The status of a reservation on hold pending an update like credit card number or flight changes.

    See: https://schema.org/ReservationHold
    Model depth: 6
    """

    type_: str = Field(default="ReservationHold", alias="@type", const=True)
