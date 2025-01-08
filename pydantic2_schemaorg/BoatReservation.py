from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Reservation import Reservation


class BoatReservation(Reservation):
    """A reservation for boat travel. Note: This type is for information about actual reservations, e.g. in confirmation
     emails or HTML pages with individual confirmations of reservations. For offers of tickets, use [[Offer]].

    See: https://schema.org/BoatReservation
    Model depth: 4
    """

    type_: str = Field(default="BoatReservation", alias="@type", const=True)
