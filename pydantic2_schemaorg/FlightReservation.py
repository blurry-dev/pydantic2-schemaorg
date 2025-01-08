from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic.v1 import Field
from pydantic2_schemaorg.Reservation import Reservation


class FlightReservation(Reservation):
    """A reservation for air travel. Note: This type is for information about actual reservations, e.g. in confirmation
     emails or HTML pages with individual confirmations of reservations. For offers of tickets, use [[Offer]].

    See: https://schema.org/FlightReservation
    Model depth: 4
    """

    type_: str = Field(default="FlightReservation", alias="@type", const=True)
    passengerPriorityStatus: Optional[
        Union[
            List[Union[str, "Text", "QualitativeValue"]],
            str,
            "Text",
            "QualitativeValue",
        ]
    ] = Field(
        default=None,
        description="The priority status assigned to a passenger for security or boarding (e.g. FastTrack or Priority).",
    )
    securityScreening: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="The type of security screening the passenger is subject to.",
    )
    passengerSequenceNumber: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = (
        Field(
            default=None,
            description="The passenger's sequence number as assigned by the airline.",
        )
    )
    boardingGroup: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="The airline-specific indicator of boarding order / preference.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.Text import Text
    from pydantic2_schemaorg.QualitativeValue import QualitativeValue
