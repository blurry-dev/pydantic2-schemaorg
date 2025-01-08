from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from pydantic.v1 import AnyUrl
from datetime import date, datetime, time


from pydantic.v1 import Field
from pydantic2_schemaorg.Intangible import Intangible


class Demand(Intangible):
    """A demand entity represents the public, not necessarily binding, not necessarily exclusive, announcement
     by an organization or person to seek a certain type of goods or services. For describing demand using this type,
     the very same properties used for Offer apply.

    See: https://schema.org/Demand
    Model depth: 3
    """

    type_: str = Field(default="Demand", alias="@type", const=True)
    warranty: Optional[
        Union[List[Union["WarrantyPromise", str]], "WarrantyPromise", str]
    ] = Field(
        default=None,
        description="The warranty promise(s) included in the offer.",
    )
    eligibleRegion: Optional[
        Union[
            List[Union[str, "Text", "Place", "GeoShape"]],
            str,
            "Text",
            "Place",
            "GeoShape",
        ]
    ] = Field(
        default=None,
        description="The ISO 3166-1 (ISO 3166-1 alpha-2) or ISO 3166-2 code, the place, or the GeoShape for the geo-political region(s) for which the offer or delivery charge specification is valid. See also [[ineligibleRegion]].",
    )
    gtin8: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="The GTIN-8 code of the product, or the product to which the offer refers. This code is also known as EAN/UCC-8 or 8-digit EAN. See [GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin) for more details.",
    )
    gtin: Optional[
        Union[List[Union[AnyUrl, "URL", str, "Text"]], AnyUrl, "URL", str, "Text"]
    ] = Field(
        default=None,
        description='A Global Trade Item Number ([GTIN](https://www.gs1.org/standards/id-keys/gtin)). GTINs identify trade items, including products and services, using numeric identification codes. A correct [[gtin]] value should be a valid GTIN, which means that it should be an all-numeric string of either 8, 12, 13 or 14 digits, or a "GS1 Digital Link" URL based on such a string. The numeric component should also have a [valid GS1 check digit](https://www.gs1.org/services/check-digit-calculator) and meet the other rules for valid GTINs. See also [GS1\'s GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin) and [Wikipedia](https://en.wikipedia.org/wiki/Global_Trade_Item_Number) for more details. Left-padding of the gtin values is not required or encouraged. The [[gtin]] property generalizes the earlier [[gtin8]], [[gtin12]], [[gtin13]], and [[gtin14]] properties. The GS1 [digital link specifications](https://www.gs1.org/standards/Digital-Link/) expresses GTINs as URLs (URIs, IRIs, etc.). Digital Links should be populated into the [[hasGS1DigitalLink]] attribute. Note also that this is a definition for how to include GTINs in Schema.org data, and not a definition of GTINs in general - see the GS1 documentation for authoritative details.',
    )
    validFrom: Optional[
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
        description="The date when the item becomes valid.",
    )
    inventoryLevel: Optional[
        Union[List[Union["QuantitativeValue", str]], "QuantitativeValue", str]
    ] = Field(
        default=None,
        description="The current approximate inventory level for the item or items.",
    )
    itemCondition: Optional[
        Union[List[Union["OfferItemCondition", str]], "OfferItemCondition", str]
    ] = Field(
        default=None,
        description="A predefined value from OfferItemCondition specifying the condition of the product or service, or the products or services included in the offer. Also used for product return policies to specify the condition of products accepted for returns.",
    )
    sku: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="The Stock Keeping Unit (SKU), i.e. a merchant-specific identifier for a product or service, or the product to which the offer refers.",
    )
    eligibleTransactionVolume: Optional[
        Union[List[Union["PriceSpecification", str]], "PriceSpecification", str]
    ] = Field(
        default=None,
        description="The transaction volume, in a monetary unit, for which the offer or price specification is valid, e.g. for indicating a minimal purchasing volume, to express free shipping above a certain order volume, or to limit the acceptance of credit cards to purchases to a certain minimal amount.",
    )
    includesObject: Optional[
        Union[List[Union["TypeAndQuantityNode", str]], "TypeAndQuantityNode", str]
    ] = Field(
        default=None,
        description="This links to a node or nodes indicating the exact quantity of the products included in an [[Offer]] or [[ProductCollection]].",
    )
    availability: Optional[
        Union[List[Union["ItemAvailability", str]], "ItemAvailability", str]
    ] = Field(
        default=None,
        description="The availability of this item&#x2014;for example In stock, Out of stock, Pre-order, etc.",
    )
    seller: Optional[
        Union[List[Union["Person", "Organization", str]], "Person", "Organization", str]
    ] = Field(
        default=None,
        description="An entity which offers (sells / leases / lends / loans) the services / goods. A seller may also be a provider.",
    )
    businessFunction: Optional[
        Union[List[Union["BusinessFunction", str]], "BusinessFunction", str]
    ] = Field(
        default=None,
        description="The business function (e.g. sell, lease, repair, dispose) of the offer or component of a bundle (TypeAndQuantityNode). The default is http://purl.org/goodrelations/v1#Sell.",
    )
    eligibleDuration: Optional[
        Union[List[Union["QuantitativeValue", str]], "QuantitativeValue", str]
    ] = Field(
        default=None,
        description="The duration for which the given offer is valid.",
    )
    eligibleCustomerType: Optional[
        Union[List[Union["BusinessEntityType", str]], "BusinessEntityType", str]
    ] = Field(
        default=None,
        description="The type(s) of customers for which the given offer is valid.",
    )
    eligibleQuantity: Optional[
        Union[List[Union["QuantitativeValue", str]], "QuantitativeValue", str]
    ] = Field(
        default=None,
        description="The interval and unit of measurement of ordering quantities for which the offer or price specification is valid. This allows e.g. specifying that a certain freight charge is valid only for a certain quantity.",
    )
    acceptedPaymentMethod: Optional[
        Union[
            List[Union["PaymentMethod", "LoanOrCredit", str]],
            "PaymentMethod",
            "LoanOrCredit",
            str,
        ]
    ] = Field(
        default=None,
        description="The payment method(s) that are accepted in general by an organization, or for some specific demand or offer.",
    )
    gtin14: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="The GTIN-14 code of the product, or the product to which the offer refers. See [GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin) for more details.",
    )
    deliveryLeadTime: Optional[
        Union[List[Union["QuantitativeValue", str]], "QuantitativeValue", str]
    ] = Field(
        default=None,
        description="The typical delay between the receipt of the order and the goods either leaving the warehouse or being prepared for pickup, in case the delivery method is on site pickup.",
    )
    serialNumber: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="The serial number or any alphanumeric identifier of a particular product. When attached to an offer, it is a shortcut for the serial number of the product included in the offer.",
    )
    gtin13: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="The GTIN-13 code of the product, or the product to which the offer refers. This is equivalent to 13-digit ISBN codes and EAN UCC-13. Former 12-digit UPC codes can be converted into a GTIN-13 code by simply adding a preceding zero. See [GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin) for more details.",
    )
    gtin12: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="The GTIN-12 code of the product, or the product to which the offer refers. The GTIN-12 is the 12-digit GS1 Identification Key composed of a U.P.C. Company Prefix, Item Reference, and Check Digit used to identify trade items. See [GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin) for more details.",
    )
    areaServed: Optional[
        Union[
            List[Union[str, "Text", "Place", "GeoShape", "AdministrativeArea"]],
            str,
            "Text",
            "Place",
            "GeoShape",
            "AdministrativeArea",
        ]
    ] = Field(
        default=None,
        description="The geographic area where a service or offered item is provided.",
    )
    asin: Optional[
        Union[List[Union[AnyUrl, "URL", str, "Text"]], AnyUrl, "URL", str, "Text"]
    ] = Field(
        default=None,
        description="An Amazon Standard Identification Number (ASIN) is a 10-character alphanumeric unique identifier assigned by Amazon.com and its partners for product identification within the Amazon organization (summary from [Wikipedia](https://en.wikipedia.org/wiki/Amazon_Standard_Identification_Number)'s article). Note also that this is a definition for how to include ASINs in Schema.org data, and not a definition of ASINs in general - see documentation from Amazon for authoritative details. ASINs are most commonly encoded as text strings, but the [asin] property supports URL/URI as potential values too.",
    )
    validThrough: Optional[
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
        description="The date after when the item is not valid. For example the end of an offer, salary period, or a period of opening hours.",
    )
    availabilityEnds: Optional[
        Union[
            List[Union[datetime, "DateTime", time, "Time", date, "Date", str]],
            datetime,
            "DateTime",
            time,
            "Time",
            date,
            "Date",
            str,
        ]
    ] = Field(
        default=None,
        description="The end of the availability of the product or service included in the offer.",
    )
    availableDeliveryMethod: Optional[
        Union[List[Union["DeliveryMethod", str]], "DeliveryMethod", str]
    ] = Field(
        default=None,
        description="The delivery method(s) available for this offer.",
    )
    priceSpecification: Optional[
        Union[List[Union["PriceSpecification", str]], "PriceSpecification", str]
    ] = Field(
        default=None,
        description="One or more detailed price specifications, indicating the unit price and delivery or payment charges.",
    )
    availabilityStarts: Optional[
        Union[
            List[Union[datetime, "DateTime", time, "Time", date, "Date", str]],
            datetime,
            "DateTime",
            time,
            "Time",
            date,
            "Date",
            str,
        ]
    ] = Field(
        default=None,
        description="The beginning of the availability of the product or service included in the offer.",
    )
    itemOffered: Optional[
        Union[
            List[
                Union[
                    "Service",
                    "Event",
                    "CreativeWork",
                    "Trip",
                    "MenuItem",
                    "Product",
                    "AggregateOffer",
                    str,
                ]
            ],
            "Service",
            "Event",
            "CreativeWork",
            "Trip",
            "MenuItem",
            "Product",
            "AggregateOffer",
            str,
        ]
    ] = Field(
        default=None,
        description="An item being offered (or demanded). The transactional nature of the offer or demand is documented using [[businessFunction]], e.g. sell, lease etc. While several common expected types are listed explicitly in this definition, others can be used. Using a second type, such as Product or a subtype of Product, can clarify the nature of the offer.",
    )
    advanceBookingRequirement: Optional[
        Union[List[Union["QuantitativeValue", str]], "QuantitativeValue", str]
    ] = Field(
        default=None,
        description="The amount of time that is required between accepting the offer and the actual usage of the resource or service.",
    )
    mpn: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="The Manufacturer Part Number (MPN) of the product, or the product to which the offer refers.",
    )
    ineligibleRegion: Optional[
        Union[
            List[Union[str, "Text", "Place", "GeoShape"]],
            str,
            "Text",
            "Place",
            "GeoShape",
        ]
    ] = Field(
        default=None,
        description="The ISO 3166-1 (ISO 3166-1 alpha-2) or ISO 3166-2 code, the place, or the GeoShape for the geo-political region(s) for which the offer or delivery charge specification is not valid, e.g. a region where the transaction is not allowed. See also [[eligibleRegion]].",
    )
    availableAtOrFrom: Optional[Union[List[Union["Place", str]], "Place", str]] = Field(
        default=None,
        description="The place(s) from which the offer can be obtained (e.g. store locations).",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.WarrantyPromise import WarrantyPromise
    from pydantic2_schemaorg.Text import Text
    from pydantic2_schemaorg.Place import Place
    from pydantic2_schemaorg.GeoShape import GeoShape
    from pydantic2_schemaorg.URL import URL
    from pydantic2_schemaorg.DateTime import DateTime
    from pydantic2_schemaorg.Date import Date
    from pydantic2_schemaorg.QuantitativeValue import QuantitativeValue
    from pydantic2_schemaorg.OfferItemCondition import OfferItemCondition
    from pydantic2_schemaorg.PriceSpecification import PriceSpecification
    from pydantic2_schemaorg.TypeAndQuantityNode import TypeAndQuantityNode
    from pydantic2_schemaorg.ItemAvailability import ItemAvailability
    from pydantic2_schemaorg.Person import Person
    from pydantic2_schemaorg.Organization import Organization
    from pydantic2_schemaorg.BusinessFunction import BusinessFunction
    from pydantic2_schemaorg.BusinessEntityType import BusinessEntityType
    from pydantic2_schemaorg.PaymentMethod import PaymentMethod
    from pydantic2_schemaorg.LoanOrCredit import LoanOrCredit
    from pydantic2_schemaorg.AdministrativeArea import AdministrativeArea
    from pydantic2_schemaorg.Time import Time
    from pydantic2_schemaorg.DeliveryMethod import DeliveryMethod
    from pydantic2_schemaorg.Service import Service
    from pydantic2_schemaorg.Event import Event
    from pydantic2_schemaorg.CreativeWork import CreativeWork
    from pydantic2_schemaorg.Trip import Trip
    from pydantic2_schemaorg.MenuItem import MenuItem
    from pydantic2_schemaorg.Product import Product
    from pydantic2_schemaorg.AggregateOffer import AggregateOffer
