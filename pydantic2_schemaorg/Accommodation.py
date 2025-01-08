from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from pydantic.v1 import AnyUrl, StrictBool, StrictInt, StrictFloat


from pydantic.v1 import Field
from pydantic2_schemaorg.Place import Place


class Accommodation(Place):
    """An accommodation is a place that can accommodate human beings, e.g. a hotel room, a camping pitch, or a meeting
     room. Many accommodations are for overnight stays, but this is not a mandatory requirement. For more specific
     types of accommodations not defined in schema.org, one can use [[additionalType]] with external vocabularies.
     <br /><br /> See also the <a href=\"/docs/hotels.html\">dedicated document on the use of schema.org for
     marking up hotels and other forms of accommodations</a>.

    See: https://schema.org/Accommodation
    Model depth: 3
    """

    type_: str = Field(default="Accommodation", alias="@type", const=True)
    permittedUsage: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="Indications regarding the permitted usage of the accommodation.",
    )
    numberOfBedrooms: Optional[
        Union[
            List[Union[StrictInt, StrictFloat, "Number", "QuantitativeValue", str]],
            StrictInt,
            StrictFloat,
            "Number",
            "QuantitativeValue",
            str,
        ]
    ] = Field(
        default=None,
        description="The total integer number of bedrooms in a some [[Accommodation]], [[ApartmentComplex]] or [[FloorPlan]].",
    )
    accommodationCategory: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = (
        Field(
            default=None,
            description="Category of an [[Accommodation]], following real estate conventions, e.g. RESO (see [PropertySubType](https://ddwiki.reso.org/display/DDW17/PropertySubType+Field), and [PropertyType](https://ddwiki.reso.org/display/DDW17/PropertyType+Field) fields for suggested values).",
        )
    )
    floorSize: Optional[
        Union[List[Union["QuantitativeValue", str]], "QuantitativeValue", str]
    ] = Field(
        default=None,
        description="The size of the accommodation, e.g. in square meter or squarefoot. Typical unit code(s): MTK for square meter, FTK for square foot, or YDK for square yard.",
    )
    occupancy: Optional[
        Union[List[Union["QuantitativeValue", str]], "QuantitativeValue", str]
    ] = Field(
        default=None,
        description="The allowed total occupancy for the accommodation in persons (including infants etc). For individual accommodations, this is not necessarily the legal maximum but defines the permitted usage as per the contractual agreement (e.g. a double room used by a single person). Typical unit code(s): C62 for person.",
    )
    petsAllowed: Optional[
        Union[
            List[Union[StrictBool, "Boolean", str, "Text"]],
            StrictBool,
            "Boolean",
            str,
            "Text",
        ]
    ] = Field(
        default=None,
        description="Indicates whether pets are allowed to enter the accommodation or lodging business. More detailed information can be put in a text value.",
    )
    numberOfFullBathrooms: Optional[
        Union[
            List[Union[StrictInt, StrictFloat, "Number", str]],
            StrictInt,
            StrictFloat,
            "Number",
            str,
        ]
    ] = Field(
        default=None,
        description="Number of full bathrooms - The total number of full and ¾ bathrooms in an [[Accommodation]]. This corresponds to the [BathroomsFull field in RESO](https://ddwiki.reso.org/display/DDW17/BathroomsFull+Field).",
    )
    numberOfPartialBathrooms: Optional[
        Union[
            List[Union[StrictInt, StrictFloat, "Number", str]],
            StrictInt,
            StrictFloat,
            "Number",
            str,
        ]
    ] = Field(
        default=None,
        description="Number of partial bathrooms - The total number of half and ¼ bathrooms in an [[Accommodation]]. This corresponds to the [BathroomsPartial field in RESO](https://ddwiki.reso.org/display/DDW17/BathroomsPartial+Field).",
    )
    floorLevel: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="The floor level for an [[Accommodation]] in a multi-storey building. Since counting systems [vary internationally](https://en.wikipedia.org/wiki/Storey#Consecutive_number_floor_designations), the local system should be used where possible.",
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
    numberOfRooms: Optional[
        Union[
            List[Union[StrictInt, StrictFloat, "Number", "QuantitativeValue", str]],
            StrictInt,
            StrictFloat,
            "Number",
            "QuantitativeValue",
            str,
        ]
    ] = Field(
        default=None,
        description="The number of rooms (excluding bathrooms and closets) of the accommodation or lodging business. Typical unit code(s): ROM for room or C62 for no unit. The type of room can be put in the unitText property of the QuantitativeValue.",
    )
    bed: Optional[
        Union[
            List[Union[str, "Text", "BedType", "BedDetails"]],
            str,
            "Text",
            "BedType",
            "BedDetails",
        ]
    ] = Field(
        default=None,
        description="The type of bed or beds included in the accommodation. For the single case of just one bed of a certain type, you use bed directly with a text. If you want to indicate the quantity of a certain kind of bed, use an instance of BedDetails. For more detailed information, use the amenityFeature property.",
    )
    yearBuilt: Optional[
        Union[
            List[Union[StrictInt, StrictFloat, "Number", str]],
            StrictInt,
            StrictFloat,
            "Number",
            str,
        ]
    ] = Field(
        default=None,
        description="The year an [[Accommodation]] was constructed. This corresponds to the [YearBuilt field in RESO](https://ddwiki.reso.org/display/DDW17/YearBuilt+Field).",
    )
    tourBookingPage: Optional[
        Union[List[Union[AnyUrl, "URL", str]], AnyUrl, "URL", str]
    ] = Field(
        default=None,
        description="A page providing information on how to book a tour of some [[Place]], such as an [[Accommodation]] or [[ApartmentComplex]] in a real estate setting, as well as other kinds of tours as appropriate.",
    )
    accommodationFloorPlan: Optional[
        Union[List[Union["FloorPlan", str]], "FloorPlan", str]
    ] = Field(
        default=None,
        description="A floorplan of some [[Accommodation]].",
    )
    numberOfBathroomsTotal: Optional[
        Union[List[Union[int, "Integer", str]], int, "Integer", str]
    ] = Field(
        default=None,
        description='The total integer number of bathrooms in some [[Accommodation]], following real estate conventions as [documented in RESO](https://ddwiki.reso.org/display/DDW17/BathroomsTotalInteger+Field): "The simple sum of the number of bathrooms. For example for a property with two Full Bathrooms and one Half Bathroom, the Bathrooms Total Integer will be 3.". See also [[numberOfRooms]].',
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.Text import Text
    from pydantic2_schemaorg.Number import Number
    from pydantic2_schemaorg.QuantitativeValue import QuantitativeValue
    from pydantic2_schemaorg.Boolean import Boolean
    from pydantic2_schemaorg.LocationFeatureSpecification import (
        LocationFeatureSpecification,
    )
    from pydantic2_schemaorg.Duration import Duration
    from pydantic2_schemaorg.BedType import BedType
    from pydantic2_schemaorg.BedDetails import BedDetails
    from pydantic2_schemaorg.URL import URL
    from pydantic2_schemaorg.FloorPlan import FloorPlan
    from pydantic2_schemaorg.Integer import Integer
