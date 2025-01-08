from __future__ import annotations
from typing import TYPE_CHECKING

from datetime import datetime, time
from typing import List, Optional, Union


from pydantic.v1 import Field
from pydantic2_schemaorg.Reservation import Reservation


class FoodEstablishmentReservation(Reservation):
    """A reservation to dine at a food-related business. Note: This type is for information about actual reservations,
     e.g. in confirmation emails or HTML pages with individual confirmations of reservations.

    See: https://schema.org/FoodEstablishmentReservation
    Model depth: 4
    """

    type_: str = Field(
        default="FoodEstablishmentReservation", alias="@type", const=True
    )
    startTime: Optional[
        Union[
            List[Union[datetime, "DateTime", time, "Time", str]],
            datetime,
            "DateTime",
            time,
            "Time",
            str,
        ]
    ] = Field(
        default=None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. E.g. John wrote a book from *January* to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file. Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions.",
    )
    endTime: Optional[
        Union[
            List[Union[datetime, "DateTime", time, "Time", str]],
            datetime,
            "DateTime",
            time,
            "Time",
            str,
        ]
    ] = Field(
        default=None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. E.g. John wrote a book from January to *December*. For media, including audio and video, it's the time offset of the end of a clip within a larger file. Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions.",
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


if TYPE_CHECKING:
    from pydantic2_schemaorg.DateTime import DateTime
    from pydantic2_schemaorg.Time import Time
    from pydantic2_schemaorg.Integer import Integer
    from pydantic2_schemaorg.QuantitativeValue import QuantitativeValue
