from __future__ import annotations
from typing import TYPE_CHECKING

from datetime import datetime
from typing import List, Optional, Union


from pydantic.v1 import Field
from pydantic2_schemaorg.Reservation import Reservation


class TaxiReservation(Reservation):
    """A reservation for a taxi. Note: This type is for information about actual reservations, e.g. in confirmation
     emails or HTML pages with individual confirmations of reservations. For offers of tickets, use [[Offer]].

    See: https://schema.org/TaxiReservation
    Model depth: 4
    """

    type_: str = Field(default="TaxiReservation", alias="@type", const=True)
    pickupTime: Optional[
        Union[List[Union[datetime, "DateTime", str]], datetime, "DateTime", str]
    ] = Field(
        default=None,
        description="When a taxi will pick up a passenger or a rental car can be picked up.",
    )
    partySize: Optional[
        Union[
            List[Union[int, "Integer", "QuantitativeValue", str]],
            int,
            "Integer",
            "QuantitativeValue",
            str,
        ]
    ] = Field(
        default=None,
        description="Number of people the reservation should accommodate.",
    )
    pickupLocation: Optional[Union[List[Union["Place", str]], "Place", str]] = Field(
        default=None,
        description="Where a taxi will pick up a passenger or a rental car can be picked up.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.DateTime import DateTime
    from pydantic2_schemaorg.Integer import Integer
    from pydantic2_schemaorg.QuantitativeValue import QuantitativeValue
    from pydantic2_schemaorg.Place import Place
