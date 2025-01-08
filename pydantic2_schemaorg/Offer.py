from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from pydantic.v1 import AnyUrl, StrictBool, StrictInt, StrictFloat
from datetime import date, datetime, time


from pydantic.v1 import Field
from pydantic2_schemaorg.Intangible import Intangible


class Offer(Intangible):
    """An offer to transfer some rights to an item or to provide a service — for example, an offer to sell tickets to an
     event, to rent the DVD of a movie, to stream a TV show over the internet, to repair a motorcycle, or to loan a book.
     Note: As the [[businessFunction]] property, which identifies the form of offer (e.g. sell, lease, repair,
     dispose), defaults to http://purl.org/goodrelations/v1#Sell; an Offer without a defined businessFunction
     value can be assumed to be an offer to sell. For [GTIN](http://www.gs1.org/barcodes/technical/idkeys/gtin)-related
     fields, see [Check Digit calculator](http://www.gs1.org/barcodes/support/check_digit_calculator)
     and [validation guide](http://www.gs1us.org/resources/standards/gtin-validation-guide) from [GS1](http://www.gs1.org/).

    See: https://schema.org/Offer
    Model depth: 3
    """

    type_: str = Field(default="Offer", alias="@type", const=True)
    warranty: Optional[
        Union[List[Union["WarrantyPromise", str]], "WarrantyPromise", str]
    ] = Field(
        default=None,
        description="The warranty promise(s) included in the offer.",
    )
    isFamilyFriendly: Optional[
        Union[List[Union[StrictBool, "Boolean", str]], StrictBool, "Boolean", str]
    ] = Field(
        default=None,
        description="Indicates whether this content is family friendly.",
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
    priceCurrency: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description='The currency of the price, or a price component when attached to [[PriceSpecification]] and its subtypes. Use standard formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217), e.g. "USD"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) for cryptocurrencies, e.g. "BTC"; well known names for [Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system) (LETS) and other currency types, e.g. "Ithaca HOUR".',
    )
    gtin8: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="The GTIN-8 code of the product, or the product to which the offer refers. This code is also known as EAN/UCC-8 or 8-digit EAN. See [GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin) for more details.",
    )
    category: Optional[
        Union[
            List[
                Union[
                    AnyUrl,
                    "URL",
                    str,
                    "Text",
                    "PhysicalActivityCategory",
                    "CategoryCode",
                    "Thing",
                ]
            ],
            AnyUrl,
            "URL",
            str,
            "Text",
            "PhysicalActivityCategory",
            "CategoryCode",
            "Thing",
        ]
    ] = Field(
        default=None,
        description="A category for the item. Greater signs or slashes can be used to informally indicate a category hierarchy.",
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
    hasGS1DigitalLink: Optional[
        Union[List[Union[AnyUrl, "URL", str]], AnyUrl, "URL", str]
    ] = Field(
        default=None,
        description='The <a href="https://www.gs1.org/standards/gs1-digital-link">GS1 digital link</a> associated with the object. This URL should conform to the particular requirements of digital links. The link should only contain the Application Identifiers (AIs) that are relevant for the entity being annotated, for instance a [[Product]] or an [[Organization]], and for the correct granularity. In particular, for products:<ul><li>A Digital Link that contains a serial number (AI <code>21</code>) should only be present on instances of [[IndividualProduct]]</li><li>A Digital Link that contains a lot number (AI <code>10</code>) should be annotated as [[SomeProduct]] if only products from that lot are sold, or [[IndividualProduct]] if there is only a specific product.</li><li>A Digital Link that contains a global model number (AI <code>8013</code>) should be attached to a [[Product]] or a [[ProductModel]].</li></ul> Other item types should be adapted similarly.',
    )
    hasAdultConsideration: Optional[
        Union[
            List[Union["AdultOrientedEnumeration", str]],
            "AdultOrientedEnumeration",
            str,
        ]
    ] = Field(
        default=None,
        description="Used to tag an item to be intended or suitable for consumption or use by adults only.",
    )
    addOn: Optional[Union[List[Union["Offer", str]], "Offer", str]] = Field(
        default=None,
        description="An additional offer that can only be obtained in combination with the first base offer (e.g. supplements and extensions that are available for a surcharge).",
    )
    hasMerchantReturnPolicy: Optional[
        Union[List[Union["MerchantReturnPolicy", str]], "MerchantReturnPolicy", str]
    ] = Field(
        default=None,
        description="Specifies a MerchantReturnPolicy that may be applicable.",
    )
    aggregateRating: Optional[
        Union[List[Union["AggregateRating", str]], "AggregateRating", str]
    ] = Field(
        default=None,
        description="The overall rating, based on a collection of reviews or ratings, of the item.",
    )
    priceValidUntil: Optional[
        Union[List[Union[date, "Date", str]], date, "Date", str]
    ] = Field(
        default=None,
        description="The date after which the price is no longer available.",
    )
    availability: Optional[
        Union[List[Union["ItemAvailability", str]], "ItemAvailability", str]
    ] = Field(
        default=None,
        description="The availability of this item&#x2014;for example In stock, Out of stock, Pre-order, etc.",
    )
    hasMeasurement: Optional[
        Union[List[Union["QuantitativeValue", str]], "QuantitativeValue", str]
    ] = Field(
        default=None,
        description="A measurement of an item, For example, the inseam of pants, the wheel size of a bicycle, the gauge of a screw, or the carbon footprint measured for certification by an authority. Usually an exact measurement, but can also be a range of measurements for adjustable products, for example belts and ski bindings.",
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
    mobileUrl: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="The [[mobileUrl]] property is provided for specific situations in which data consumers need to determine whether one of several provided URLs is a dedicated 'mobile site'. To discourage over-use, and reflecting intial usecases, the property is expected only on [[Product]] and [[Offer]], rather than [[Thing]]. The general trend in web technology is towards [responsive design](https://en.wikipedia.org/wiki/Responsive_web_design) in which content can be flexibly adapted to a wide range of browsing environments. Pages and sites referenced with the long-established [[url]] property should ideally also be usable on a wide variety of devices, including mobile phones. In most cases, it would be pointless and counter productive to attempt to update all [[url]] markup to use [[mobileUrl]] for more mobile-oriented pages. The property is intended for the case when items (primarily [[Product]] and [[Offer]]) have extra URLs hosted on an additional \"mobile site\" alongside the main one. It should not be taken as an endorsement of this publication style.",
    )
    offeredBy: Optional[
        Union[List[Union["Person", "Organization", str]], "Person", "Organization", str]
    ] = Field(
        default=None,
        description="A pointer to the organization or person making the offer.",
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
    validForMemberTier: Optional[
        Union[List[Union["MemberProgramTier", str]], "MemberProgramTier", str]
    ] = Field(
        default=None,
        description="The membership program tier an Offer (or a PriceSpecification, OfferShippingDetails, or MerchantReturnPolicy under an Offer) is valid for.",
    )
    gtin13: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="The GTIN-13 code of the product, or the product to which the offer refers. This is equivalent to 13-digit ISBN codes and EAN UCC-13. Former 12-digit UPC codes can be converted into a GTIN-13 code by simply adding a preceding zero. See [GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin) for more details.",
    )
    review: Optional[Union[List[Union["Review", str]], "Review", str]] = Field(
        default=None,
        description="A review of the item.",
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
    price: Optional[
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
        description="The offer price of a product, or of a price component when attached to PriceSpecification and its subtypes. Usage guidelines: * Use the [[priceCurrency]] property (with standard formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217), e.g. \"USD\"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) for cryptocurrencies, e.g. \"BTC\"; well known names for [Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system) (LETS) and other currency types, e.g. \"Ithaca HOUR\") instead of including [ambiguous symbols](http://en.wikipedia.org/wiki/Dollar_sign#Currencies_that_use_the_dollar_or_peso_sign) such as '$' in the value. * Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid using these symbols as a readability separator. * Note that both [RDFa](http://www.w3.org/TR/xhtml-rdfa-primer/#using-the-content-attribute) and Microdata syntax allow the use of a \"content=\" attribute for publishing simple machine-readable values alongside more human-friendly formatting. * Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similar Unicode symbols.",
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
    additionalProperty: Optional[
        Union[List[Union["PropertyValue", str]], "PropertyValue", str]
    ] = Field(
        default=None,
        description="A property-value pair representing an additional characteristic of the entity, e.g. a product feature or another characteristic for which there is no matching property in schema.org. Note: Publishers should be aware that applications designed to use specific schema.org properties (e.g. https://schema.org/width, https://schema.org/color, https://schema.org/gtin13, ...) will typically expect such data to be provided using those properties, rather than using the generic property/value mechanism.",
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
    checkoutPageURLTemplate: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = (
        Field(
            default=None,
            description="A URL template (RFC 6570) for a checkout page for an offer. This approach allows merchants to specify a URL for online checkout of the offered product, by interpolating parameters such as the logged in user ID, product ID, quantity, discount code etc. Parameter naming and standardization are not specified here.",
        )
    )
    leaseLength: Optional[
        Union[
            List[Union["Duration", "QuantitativeValue", str]],
            "Duration",
            "QuantitativeValue",
            str,
        ]
    ] = Field(
        default=None,
        description="Length of the lease for some [[Accommodation]], either particular to some [[Offer]] or in some cases intrinsic to the property.",
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
    shippingDetails: Optional[
        Union[List[Union["OfferShippingDetails", str]], "OfferShippingDetails", str]
    ] = Field(
        default=None,
        description="Indicates information about the shipping policies and options associated with an [[Offer]].",
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
    reviews: Optional[Union[List[Union["Review", str]], "Review", str]] = Field(
        default=None,
        description="Review of the item.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.WarrantyPromise import WarrantyPromise
    from pydantic2_schemaorg.Boolean import Boolean
    from pydantic2_schemaorg.Text import Text
    from pydantic2_schemaorg.Place import Place
    from pydantic2_schemaorg.GeoShape import GeoShape
    from pydantic2_schemaorg.URL import URL
    from pydantic2_schemaorg.PhysicalActivityCategory import PhysicalActivityCategory
    from pydantic2_schemaorg.CategoryCode import CategoryCode
    from pydantic2_schemaorg.Thing import Thing
    from pydantic2_schemaorg.DateTime import DateTime
    from pydantic2_schemaorg.Date import Date
    from pydantic2_schemaorg.QuantitativeValue import QuantitativeValue
    from pydantic2_schemaorg.OfferItemCondition import OfferItemCondition
    from pydantic2_schemaorg.PriceSpecification import PriceSpecification
    from pydantic2_schemaorg.TypeAndQuantityNode import TypeAndQuantityNode
    from pydantic2_schemaorg.AdultOrientedEnumeration import AdultOrientedEnumeration
    from pydantic2_schemaorg.MerchantReturnPolicy import MerchantReturnPolicy
    from pydantic2_schemaorg.AggregateRating import AggregateRating
    from pydantic2_schemaorg.ItemAvailability import ItemAvailability
    from pydantic2_schemaorg.Person import Person
    from pydantic2_schemaorg.Organization import Organization
    from pydantic2_schemaorg.BusinessFunction import BusinessFunction
    from pydantic2_schemaorg.BusinessEntityType import BusinessEntityType
    from pydantic2_schemaorg.PaymentMethod import PaymentMethod
    from pydantic2_schemaorg.LoanOrCredit import LoanOrCredit
    from pydantic2_schemaorg.MemberProgramTier import MemberProgramTier
    from pydantic2_schemaorg.Review import Review
    from pydantic2_schemaorg.AdministrativeArea import AdministrativeArea
    from pydantic2_schemaorg.Number import Number
    from pydantic2_schemaorg.Time import Time
    from pydantic2_schemaorg.PropertyValue import PropertyValue
    from pydantic2_schemaorg.DeliveryMethod import DeliveryMethod
    from pydantic2_schemaorg.Duration import Duration
    from pydantic2_schemaorg.OfferShippingDetails import OfferShippingDetails
    from pydantic2_schemaorg.Service import Service
    from pydantic2_schemaorg.Event import Event
    from pydantic2_schemaorg.CreativeWork import CreativeWork
    from pydantic2_schemaorg.Trip import Trip
    from pydantic2_schemaorg.MenuItem import MenuItem
    from pydantic2_schemaorg.Product import Product
    from pydantic2_schemaorg.AggregateOffer import AggregateOffer
