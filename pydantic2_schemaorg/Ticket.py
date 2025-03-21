from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from pydantic.v1 import AnyUrl, StrictInt, StrictFloat
from datetime import date, datetime


from pydantic.v1 import Field
from pydantic2_schemaorg.Intangible import Intangible


class Ticket(Intangible):
    """Used to describe a ticket to an event, a flight, a bus ride, etc.

    See: https://schema.org/Ticket
    Model depth: 3
    """

    type_: str = Field(default="Ticket", alias="@type", const=True)
    priceCurrency: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description='The currency of the price, or a price component when attached to [[PriceSpecification]] and its subtypes. Use standard formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217), e.g. "USD"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) for cryptocurrencies, e.g. "BTC"; well known names for [Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system) (LETS) and other currency types, e.g. "Ithaca HOUR".',
    )
    totalPrice: Optional[
        Union[
            List[
                Union[
                    StrictInt, StrictFloat, "Number", str, "Text", "PriceSpecification"
                ]
            ],
            StrictInt,
            StrictFloat,
            "Number",
            str,
            "Text",
            "PriceSpecification",
        ]
    ] = Field(
        default=None,
        description="The total price for the reservation or ticket, including applicable taxes, shipping, etc. Usage guidelines: * Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similar Unicode symbols. * Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid using these symbols as a readability separator.",
    )
    dateIssued: Optional[
        Union[
            List[Union[datetime, "DateTime", date, "Date", str]],
            datetime,
            "DateTime",
            date,
            "Date",
            str,
        ]
    ] = Field(
        default=None,
        description="The date the ticket was issued.",
    )
    underName: Optional[
        Union[List[Union["Person", "Organization", str]], "Person", "Organization", str]
    ] = Field(
        default=None,
        description="The person or organization the reservation or ticket is for.",
    )
    issuedBy: Optional[Union[List[Union["Organization", str]], "Organization", str]] = (
        Field(
            default=None,
            description="The organization issuing the item, for example a [[Permit]], [[Ticket]], or [[Certification]].",
        )
    )
    ticketToken: Optional[
        Union[List[Union[AnyUrl, "URL", str, "Text"]], AnyUrl, "URL", str, "Text"]
    ] = Field(
        default=None,
        description="Reference to an asset (e.g., Barcode, QR code image or PDF) usable for entrance.",
    )
    ticketedSeat: Optional[Union[List[Union["Seat", str]], "Seat", str]] = Field(
        default=None,
        description="The seat associated with the ticket.",
    )
    ticketNumber: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="The unique identifier for the ticket.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.Text import Text
    from pydantic2_schemaorg.Number import Number
    from pydantic2_schemaorg.PriceSpecification import PriceSpecification
    from pydantic2_schemaorg.DateTime import DateTime
    from pydantic2_schemaorg.Date import Date
    from pydantic2_schemaorg.Person import Person
    from pydantic2_schemaorg.Organization import Organization
    from pydantic2_schemaorg.URL import URL
    from pydantic2_schemaorg.Seat import Seat
