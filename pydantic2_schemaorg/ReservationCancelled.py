from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.ReservationStatusType import ReservationStatusType


class ReservationCancelled(ReservationStatusType):
    """The status for a previously confirmed reservation that is now cancelled.

    See: https://schema.org/ReservationCancelled
    Model depth: 6
    """

    type_: str = Field(default="ReservationCancelled", alias="@type", const=True)
