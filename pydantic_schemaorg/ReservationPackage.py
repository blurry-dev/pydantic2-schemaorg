from pydantic import Field
from pydantic_schemaorg.Reservation import Reservation
from typing import List, Optional, Union, Any


class ReservationPackage(Reservation):
    """A group of multiple reservations with common values for all sub-reservations.

    See https://schema.org/ReservationPackage.

    """

    subReservation: Optional[Union[List[Reservation], Reservation]] = Field(
        None,
        description="The individual reservations included in the package. Typically a repeated property.",
    )
    locals().update({"@type": Field("ReservationPackage", const=True)})


ReservationPackage.update_forward_refs()