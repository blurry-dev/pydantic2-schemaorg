from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date


from pydantic import Field
from pydantic_schemaorg.Reservation import Reservation


class RentalCarReservation(Reservation):
    """A reservation for a rental car. Note: This type is for information about actual reservations,"
     "e.g. in confirmation emails or HTML pages with individual confirmations of reservations.

    See: https://schema.org/RentalCarReservation
    Model depth: 4
    """
    type_: str = Field(default="RentalCarReservation", alias='@type', constant=True)
    pickupLocation: Optional[Union[List[Union['Place', str]], 'Place', str]] = Field(
        default=None,
        description="Where a taxi will pick up a passenger or a rental car can be picked up.",
    )
    dropoffLocation: Optional[Union[List[Union['Place', str]], 'Place', str]] = Field(
        default=None,
        description="Where a rental car can be dropped off.",
    )
    pickupTime: Optional[Union[List[Union[ISO8601Date, 'DateTime', str]], ISO8601Date, 'DateTime', str]] = Field(
        default=None,
        description="When a taxi will pickup a passenger or a rental car can be picked up.",
    )
    dropoffTime: Optional[Union[List[Union[ISO8601Date, 'DateTime', str]], ISO8601Date, 'DateTime', str]] = Field(
        default=None,
        description="When a rental car can be dropped off.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Place import Place
    from pydantic_schemaorg.DateTime import DateTime
