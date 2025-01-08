from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from pydantic.v1 import AnyUrl, StrictBool, StrictInt, StrictFloat


from pydantic.v1 import Field
from pydantic2_schemaorg.Thing import Thing


class Place(Thing):
    """Entities that have a somewhat fixed, physical extension.

    See: https://schema.org/Place
    Model depth: 2
    """

    type_: str = Field(default="Place", alias="@type", const=True)
    containedIn: Optional[Union[List[Union["Place", str]], "Place", str]] = Field(
        default=None,
        description="The basic containment relation between a place and one that contains it.",
    )
    maximumAttendeeCapacity: Optional[
        Union[List[Union[int, "Integer", str]], int, "Integer", str]
    ] = Field(
        default=None,
        description="The total number of individuals that may attend an event or venue.",
    )
    maps: Optional[Union[List[Union[AnyUrl, "URL", str]], AnyUrl, "URL", str]] = Field(
        default=None,
        description="A URL to a map of the place.",
    )
    geoWithin: Optional[
        Union[
            List[Union["GeospatialGeometry", "Place", str]],
            "GeospatialGeometry",
            "Place",
            str,
        ]
    ] = Field(
        default=None,
        description="Represents a relationship between two geometries (or the places they represent), relating a geometry to one that contains it, i.e. it is inside (i.e. within) its interior. As defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).",
    )
    faxNumber: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="The fax number.",
    )
    geoCovers: Optional[
        Union[
            List[Union["GeospatialGeometry", "Place", str]],
            "GeospatialGeometry",
            "Place",
            str,
        ]
    ] = Field(
        default=None,
        description='Represents a relationship between two geometries (or the places they represent), relating a covering geometry to a covered geometry. "Every point of b is a point of (the interior or boundary of) a". As defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).',
    )
    branchCode: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description='A short textual code (also called "store code") that uniquely identifies a place of business. The code is typically assigned by the parentOrganization and used in structured URLs. For example, in the URL http://www.starbucks.co.uk/store-locator/etc/detail/3047 the code "3047" is a branchCode for a particular branch.',
    )
    logo: Optional[
        Union[
            List[Union[AnyUrl, "URL", "ImageObject", str]],
            AnyUrl,
            "URL",
            "ImageObject",
            str,
        ]
    ] = Field(
        default=None,
        description="An associated logo.",
    )
    containsPlace: Optional[Union[List[Union["Place", str]], "Place", str]] = Field(
        default=None,
        description="The basic containment relation between a place and another that it contains.",
    )
    geoOverlaps: Optional[
        Union[
            List[Union["GeospatialGeometry", "Place", str]],
            "GeospatialGeometry",
            "Place",
            str,
        ]
    ] = Field(
        default=None,
        description="Represents a relationship between two geometries (or the places they represent), relating a geometry to another that geospatially overlaps it, i.e. they have some but not all points in common. As defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).",
    )
    hasGS1DigitalLink: Optional[
        Union[List[Union[AnyUrl, "URL", str]], AnyUrl, "URL", str]
    ] = Field(
        default=None,
        description='The <a href="https://www.gs1.org/standards/gs1-digital-link">GS1 digital link</a> associated with the object. This URL should conform to the particular requirements of digital links. The link should only contain the Application Identifiers (AIs) that are relevant for the entity being annotated, for instance a [[Product]] or an [[Organization]], and for the correct granularity. In particular, for products:<ul><li>A Digital Link that contains a serial number (AI <code>21</code>) should only be present on instances of [[IndividualProduct]]</li><li>A Digital Link that contains a lot number (AI <code>10</code>) should be annotated as [[SomeProduct]] if only products from that lot are sold, or [[IndividualProduct]] if there is only a specific product.</li><li>A Digital Link that contains a global model number (AI <code>8013</code>) should be attached to a [[Product]] or a [[ProductModel]].</li></ul> Other item types should be adapted similarly.',
    )
    hasCertification: Optional[
        Union[List[Union["Certification", str]], "Certification", str]
    ] = Field(
        default=None,
        description="Certification information about a product, organization, service, place, or person.",
    )
    longitude: Optional[
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
        description="The longitude of a location. For example ```-122.08585``` ([WGS 84](https://en.wikipedia.org/wiki/World_Geodetic_System)).",
    )
    photo: Optional[
        Union[
            List[Union["Photograph", "ImageObject", str]],
            "Photograph",
            "ImageObject",
            str,
        ]
    ] = Field(
        default=None,
        description="A photograph of this place.",
    )
    aggregateRating: Optional[
        Union[List[Union["AggregateRating", str]], "AggregateRating", str]
    ] = Field(
        default=None,
        description="The overall rating, based on a collection of reviews or ratings, of the item.",
    )
    map: Optional[Union[List[Union[AnyUrl, "URL", str]], AnyUrl, "URL", str]] = Field(
        default=None,
        description="A URL to a map of the place.",
    )
    keywords: Optional[
        Union[
            List[Union[AnyUrl, "URL", str, "Text", "DefinedTerm"]],
            AnyUrl,
            "URL",
            str,
            "Text",
            "DefinedTerm",
        ]
    ] = Field(
        default=None,
        description="Keywords or tags used to describe some item. Multiple textual entries in a keywords list are typically delimited by commas, or by repeating the property.",
    )
    geoDisjoint: Optional[
        Union[
            List[Union["GeospatialGeometry", "Place", str]],
            "GeospatialGeometry",
            "Place",
            str,
        ]
    ] = Field(
        default=None,
        description='Represents spatial relations in which two geometries (or the places they represent) are topologically disjoint: "they have no point in common. They form a set of disconnected geometries." (A symmetric relationship, as defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).)',
    )
    isAccessibleForFree: Optional[
        Union[List[Union[StrictBool, "Boolean", str]], StrictBool, "Boolean", str]
    ] = Field(
        default=None,
        description="A flag to signal that the item, event, or place is accessible for free.",
    )
    geoCrosses: Optional[
        Union[
            List[Union["GeospatialGeometry", "Place", str]],
            "GeospatialGeometry",
            "Place",
            str,
        ]
    ] = Field(
        default=None,
        description='Represents a relationship between two geometries (or the places they represent), relating a geometry to another that crosses it: "a crosses b: they have some but not all interior points in common, and the dimension of the intersection is less than that of at least one of them". As defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).',
    )
    latitude: Optional[
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
        description="The latitude of a location. For example ```37.42242``` ([WGS 84](https://en.wikipedia.org/wiki/World_Geodetic_System)).",
    )
    isicV4: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="The International Standard of Industrial Classification of All Economic Activities (ISIC), Revision 4 code for a particular organization, business person, or place.",
    )
    geoTouches: Optional[
        Union[
            List[Union["GeospatialGeometry", "Place", str]],
            "GeospatialGeometry",
            "Place",
            str,
        ]
    ] = Field(
        default=None,
        description='Represents spatial relations in which two geometries (or the places they represent) touch: "they have at least one boundary point in common, but no interior points." (A symmetric relationship, as defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).)',
    )
    containedInPlace: Optional[Union[List[Union["Place", str]], "Place", str]] = Field(
        default=None,
        description="The basic containment relation between a place and one that contains it.",
    )
    publicAccess: Optional[
        Union[List[Union[StrictBool, "Boolean", str]], StrictBool, "Boolean", str]
    ] = Field(
        default=None,
        description="A flag to signal that the [[Place]] is open to public visitors. If this property is omitted there is no assumed default boolean value.",
    )
    openingHoursSpecification: Optional[
        Union[
            List[Union["OpeningHoursSpecification", str]],
            "OpeningHoursSpecification",
            str,
        ]
    ] = Field(
        default=None,
        description="The opening hours of a certain place.",
    )
    globalLocationNumber: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = (
        Field(
            default=None,
            description="The [Global Location Number](http://www.gs1.org/gln) (GLN, sometimes also referred to as International Location Number or ILN) of the respective organization, person, or place. The GLN is a 13-digit number used to identify parties and physical locations.",
        )
    )
    slogan: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="A slogan or motto associated with the item.",
    )
    event: Optional[Union[List[Union["Event", str]], "Event", str]] = Field(
        default=None,
        description="Upcoming or past event associated with this place, organization, or action.",
    )
    hasDriveThroughService: Optional[
        Union[List[Union[StrictBool, "Boolean", str]], StrictBool, "Boolean", str]
    ] = Field(
        default=None,
        description="Indicates whether some facility (e.g. [[FoodEstablishment]], [[CovidTestingFacility]]) offers a service that can be used by driving through in a car. In the case of [[CovidTestingFacility]] such facilities could potentially help with social distancing from other potentially-infected users.",
    )
    geoContains: Optional[
        Union[
            List[Union["GeospatialGeometry", "Place", str]],
            "GeospatialGeometry",
            "Place",
            str,
        ]
    ] = Field(
        default=None,
        description='Represents a relationship between two geometries (or the places they represent), relating a containing geometry to a contained geometry. "a contains b iff no points of b lie in the exterior of a, and at least one point of the interior of b lies in the interior of a". As defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).',
    )
    geoCoveredBy: Optional[
        Union[
            List[Union["GeospatialGeometry", "Place", str]],
            "GeospatialGeometry",
            "Place",
            str,
        ]
    ] = Field(
        default=None,
        description="Represents a relationship between two geometries (or the places they represent), relating a geometry to another that covers it. As defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).",
    )
    review: Optional[Union[List[Union["Review", str]], "Review", str]] = Field(
        default=None,
        description="A review of the item.",
    )
    amenityFeature: Optional[
        Union[
            List[Union["LocationFeatureSpecification", str]],
            "LocationFeatureSpecification",
            str,
        ]
    ] = Field(
        default=None,
        description="An amenity feature (e.g. a characteristic or service) of the Accommodation. This generic property does not make a statement about whether the feature is included in an offer for the main accommodation or available at extra costs.",
    )
    geo: Optional[
        Union[
            List[Union["GeoCoordinates", "GeoShape", str]],
            "GeoCoordinates",
            "GeoShape",
            str,
        ]
    ] = Field(
        default=None,
        description="The geo coordinates of the place.",
    )
    additionalProperty: Optional[
        Union[List[Union["PropertyValue", str]], "PropertyValue", str]
    ] = Field(
        default=None,
        description="A property-value pair representing an additional characteristic of the entity, e.g. a product feature or another characteristic for which there is no matching property in schema.org. Note: Publishers should be aware that applications designed to use specific schema.org properties (e.g. https://schema.org/width, https://schema.org/color, https://schema.org/gtin13, ...) will typically expect such data to be provided using those properties, rather than using the generic property/value mechanism.",
    )
    geoIntersects: Optional[
        Union[
            List[Union["GeospatialGeometry", "Place", str]],
            "GeospatialGeometry",
            "Place",
            str,
        ]
    ] = Field(
        default=None,
        description="Represents spatial relations in which two geometries (or the places they represent) have at least one point in common. As defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).",
    )
    geoEquals: Optional[
        Union[
            List[Union["GeospatialGeometry", "Place", str]],
            "GeospatialGeometry",
            "Place",
            str,
        ]
    ] = Field(
        default=None,
        description='Represents spatial relations in which two geometries (or the places they represent) are topologically equal, as defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM). "Two geometries are topologically equal if their interiors intersect and no part of the interior or boundary of one geometry intersects the exterior of the other" (a symmetric relationship).',
    )
    tourBookingPage: Optional[
        Union[List[Union[AnyUrl, "URL", str]], AnyUrl, "URL", str]
    ] = Field(
        default=None,
        description="A page providing information on how to book a tour of some [[Place]], such as an [[Accommodation]] or [[ApartmentComplex]] in a real estate setting, as well as other kinds of tours as appropriate.",
    )
    photos: Optional[
        Union[
            List[Union["Photograph", "ImageObject", str]],
            "Photograph",
            "ImageObject",
            str,
        ]
    ] = Field(
        default=None,
        description="Photographs of this place.",
    )
    hasMap: Optional[
        Union[List[Union[AnyUrl, "URL", "Map", str]], AnyUrl, "URL", "Map", str]
    ] = Field(
        default=None,
        description="A URL to a map of the place.",
    )
    specialOpeningHoursSpecification: Optional[
        Union[
            List[Union["OpeningHoursSpecification", str]],
            "OpeningHoursSpecification",
            str,
        ]
    ] = Field(
        default=None,
        description="The special opening hours of a certain place. Use this to explicitly override general opening hours brought in scope by [[openingHoursSpecification]] or [[openingHours]].",
    )
    smokingAllowed: Optional[
        Union[List[Union[StrictBool, "Boolean", str]], StrictBool, "Boolean", str]
    ] = Field(
        default=None,
        description="Indicates whether it is allowed to smoke in the place, e.g. in the restaurant, hotel or hotel room.",
    )
    telephone: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="The telephone number.",
    )
    address: Optional[
        Union[List[Union[str, "Text", "PostalAddress"]], str, "Text", "PostalAddress"]
    ] = Field(
        default=None,
        description="Physical address of the item.",
    )
    reviews: Optional[Union[List[Union["Review", str]], "Review", str]] = Field(
        default=None,
        description="Review of the item.",
    )
    events: Optional[Union[List[Union["Event", str]], "Event", str]] = Field(
        default=None,
        description="Upcoming or past events associated with this place or organization.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.Integer import Integer
    from pydantic2_schemaorg.URL import URL
    from pydantic2_schemaorg.GeospatialGeometry import GeospatialGeometry
    from pydantic2_schemaorg.Text import Text
    from pydantic2_schemaorg.ImageObject import ImageObject
    from pydantic2_schemaorg.Certification import Certification
    from pydantic2_schemaorg.Number import Number
    from pydantic2_schemaorg.Photograph import Photograph
    from pydantic2_schemaorg.AggregateRating import AggregateRating
    from pydantic2_schemaorg.DefinedTerm import DefinedTerm
    from pydantic2_schemaorg.Boolean import Boolean
    from pydantic2_schemaorg.OpeningHoursSpecification import OpeningHoursSpecification
    from pydantic2_schemaorg.Event import Event
    from pydantic2_schemaorg.Review import Review
    from pydantic2_schemaorg.LocationFeatureSpecification import (
        LocationFeatureSpecification,
    )
    from pydantic2_schemaorg.GeoCoordinates import GeoCoordinates
    from pydantic2_schemaorg.GeoShape import GeoShape
    from pydantic2_schemaorg.PropertyValue import PropertyValue
    from pydantic2_schemaorg.Map import Map
    from pydantic2_schemaorg.PostalAddress import PostalAddress
