from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from pydantic.v1 import AnyUrl
from datetime import date, datetime


from pydantic.v1 import Field
from pydantic2_schemaorg.Intangible import Intangible


class ParcelDelivery(Intangible):
    """The delivery of a parcel either via the postal service or a commercial service.

    See: https://schema.org/ParcelDelivery
    Model depth: 3
    """

    type_: str = Field(default="ParcelDelivery", alias="@type", const=True)
    originAddress: Optional[
        Union[List[Union["PostalAddress", str]], "PostalAddress", str]
    ] = Field(
        default=None,
        description="Shipper's address.",
    )
    partOfOrder: Optional[Union[List[Union["Order", str]], "Order", str]] = Field(
        default=None,
        description="The overall order the items in this delivery were included in.",
    )
    deliveryStatus: Optional[
        Union[List[Union["DeliveryEvent", str]], "DeliveryEvent", str]
    ] = Field(
        default=None,
        description="New entry added as the package passes through each leg of its journey (from shipment to final delivery).",
    )
    deliveryAddress: Optional[
        Union[List[Union["PostalAddress", str]], "PostalAddress", str]
    ] = Field(
        default=None,
        description="Destination address.",
    )
    hasDeliveryMethod: Optional[
        Union[List[Union["DeliveryMethod", str]], "DeliveryMethod", str]
    ] = Field(
        default=None,
        description="Method used for delivery or shipping.",
    )
    trackingUrl: Optional[
        Union[List[Union[AnyUrl, "URL", str]], AnyUrl, "URL", str]
    ] = Field(
        default=None,
        description="Tracking url for the parcel delivery.",
    )
    itemShipped: Optional[Union[List[Union["Product", str]], "Product", str]] = Field(
        default=None,
        description="Item(s) being shipped.",
    )
    expectedArrivalFrom: Optional[
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
        description="The earliest date the package may arrive.",
    )
    provider: Optional[
        Union[List[Union["Person", "Organization", str]], "Person", "Organization", str]
    ] = Field(
        default=None,
        description="The service provider, service operator, or service performer; the goods producer. Another party (a seller) may offer those services or goods on behalf of the provider. A provider may also serve as the seller.",
    )
    trackingNumber: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="Shipper tracking number.",
    )
    expectedArrivalUntil: Optional[
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
        description="The latest date the package may arrive.",
    )
    carrier: Optional[Union[List[Union["Organization", str]], "Organization", str]] = (
        Field(
            default=None,
            description="'carrier' is an out-dated term indicating the 'provider' for parcel delivery and flights.",
        )
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.PostalAddress import PostalAddress
    from pydantic2_schemaorg.Order import Order
    from pydantic2_schemaorg.DeliveryEvent import DeliveryEvent
    from pydantic2_schemaorg.DeliveryMethod import DeliveryMethod
    from pydantic2_schemaorg.URL import URL
    from pydantic2_schemaorg.Product import Product
    from pydantic2_schemaorg.DateTime import DateTime
    from pydantic2_schemaorg.Date import Date
    from pydantic2_schemaorg.Person import Person
    from pydantic2_schemaorg.Organization import Organization
    from pydantic2_schemaorg.Text import Text
