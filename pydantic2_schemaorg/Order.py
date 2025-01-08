from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from datetime import date, datetime
from pydantic.v1 import AnyUrl, StrictBool, StrictInt, StrictFloat


from pydantic.v1 import Field
from pydantic2_schemaorg.Intangible import Intangible


class Order(Intangible):
    """An order is a confirmation of a transaction (a receipt), which can contain multiple line items, each represented
     by an Offer that has been accepted by the customer.

    See: https://schema.org/Order
    Model depth: 3
    """

    type_: str = Field(default="Order", alias="@type", const=True)
    discountCode: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="Code used to redeem a discount.",
    )
    orderDate: Optional[
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
        description="Date order was placed.",
    )
    merchant: Optional[
        Union[List[Union["Person", "Organization", str]], "Person", "Organization", str]
    ] = Field(
        default=None,
        description="'merchant' is an out-dated term for 'seller'.",
    )
    paymentMethod: Optional[
        Union[List[Union["PaymentMethod", str]], "PaymentMethod", str]
    ] = Field(
        default=None,
        description="The name of the credit card or other method of payment for the order.",
    )
    isGift: Optional[
        Union[List[Union[StrictBool, "Boolean", str]], StrictBool, "Boolean", str]
    ] = Field(
        default=None,
        description="Indicates whether the offer was accepted as a gift for someone other than the buyer.",
    )
    orderDelivery: Optional[
        Union[List[Union["ParcelDelivery", str]], "ParcelDelivery", str]
    ] = Field(
        default=None,
        description="The delivery of the parcel related to this order or order item.",
    )
    paymentDue: Optional[
        Union[List[Union[datetime, "DateTime", str]], datetime, "DateTime", str]
    ] = Field(
        default=None,
        description="The date that payment is due.",
    )
    acceptedOffer: Optional[Union[List[Union["Offer", str]], "Offer", str]] = Field(
        default=None,
        description="The offer(s) -- e.g., product, quantity and price combinations -- included in the order.",
    )
    seller: Optional[
        Union[List[Union["Person", "Organization", str]], "Person", "Organization", str]
    ] = Field(
        default=None,
        description="An entity which offers (sells / leases / lends / loans) the services / goods. A seller may also be a provider.",
    )
    discount: Optional[
        Union[
            List[Union[StrictInt, StrictFloat, "Number", str, "Text"]],
            StrictInt,
            StrictFloat,
            "Number",
            str,
            "Text",
        ]
    ] = Field(
        default=None,
        description="Any discount applied (to an Order).",
    )
    paymentDueDate: Optional[
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
        description="The date that payment is due.",
    )
    discountCurrency: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description='The currency of the discount. Use standard formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217), e.g. "USD"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) for cryptocurrencies, e.g. "BTC"; well known names for [Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system) (LETS) and other currency types, e.g. "Ithaca HOUR".',
    )
    broker: Optional[
        Union[List[Union["Person", "Organization", str]], "Person", "Organization", str]
    ] = Field(
        default=None,
        description="An entity that arranges for an exchange between a buyer and a seller. In most cases a broker never acquires or releases ownership of a product or service involved in an exchange. If it is not clear whether an entity is a broker, seller, or buyer, the latter two terms are preferred.",
    )
    billingAddress: Optional[
        Union[List[Union["PostalAddress", str]], "PostalAddress", str]
    ] = Field(
        default=None,
        description="The billing address for the order.",
    )
    paymentUrl: Optional[Union[List[Union[AnyUrl, "URL", str]], AnyUrl, "URL", str]] = (
        Field(
            default=None,
            description="The URL for sending a payment.",
        )
    )
    orderedItem: Optional[
        Union[
            List[Union["OrderItem", "Service", "Product", str]],
            "OrderItem",
            "Service",
            "Product",
            str,
        ]
    ] = Field(
        default=None,
        description="The item ordered.",
    )
    confirmationNumber: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="A number that confirms the given order or payment has been received.",
    )
    partOfInvoice: Optional[Union[List[Union["Invoice", str]], "Invoice", str]] = Field(
        default=None,
        description="The order is being paid as part of the referenced Invoice.",
    )
    orderStatus: Optional[
        Union[List[Union["OrderStatus", str]], "OrderStatus", str]
    ] = Field(
        default=None,
        description="The current status of the order.",
    )
    orderNumber: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="The identifier of the transaction.",
    )
    customer: Optional[
        Union[List[Union["Person", "Organization", str]], "Person", "Organization", str]
    ] = Field(
        default=None,
        description="Party placing the order or paying the invoice.",
    )
    paymentMethodId: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="An identifier for the method of payment used (e.g. the last 4 digits of the credit card).",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.Text import Text
    from pydantic2_schemaorg.DateTime import DateTime
    from pydantic2_schemaorg.Date import Date
    from pydantic2_schemaorg.Person import Person
    from pydantic2_schemaorg.Organization import Organization
    from pydantic2_schemaorg.PaymentMethod import PaymentMethod
    from pydantic2_schemaorg.Boolean import Boolean
    from pydantic2_schemaorg.ParcelDelivery import ParcelDelivery
    from pydantic2_schemaorg.Offer import Offer
    from pydantic2_schemaorg.Number import Number
    from pydantic2_schemaorg.PostalAddress import PostalAddress
    from pydantic2_schemaorg.URL import URL
    from pydantic2_schemaorg.OrderItem import OrderItem
    from pydantic2_schemaorg.Service import Service
    from pydantic2_schemaorg.Product import Product
    from pydantic2_schemaorg.Invoice import Invoice
    from pydantic2_schemaorg.OrderStatus import OrderStatus
