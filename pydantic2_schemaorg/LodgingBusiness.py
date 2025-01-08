from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from datetime import datetime, time
from pydantic.v1 import StrictBool, StrictInt, StrictFloat


from pydantic.v1 import Field
from pydantic2_schemaorg.LocalBusiness import LocalBusiness


class LodgingBusiness(LocalBusiness):
    """A lodging business, such as a motel, hotel, or inn.

    See: https://schema.org/LodgingBusiness
    Model depth: 4
    """

    type_: str = Field(default="LodgingBusiness", alias="@type", const=True)
    audience: Optional[Union[List[Union["Audience", str]], "Audience", str]] = Field(
        default=None,
        description="An intended audience, i.e. a group for whom something was created.",
    )
    availableLanguage: Optional[
        Union[List[Union[str, "Text", "Language"]], str, "Text", "Language"]
    ] = Field(
        default=None,
        description="A language someone may use with or at the item, service or place. Please use one of the language codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47). See also [[inLanguage]].",
    )
    checkoutTime: Optional[
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
        description="The latest someone may check out of a lodging establishment.",
    )
    starRating: Optional[Union[List[Union["Rating", str]], "Rating", str]] = Field(
        default=None,
        description="An official rating for a lodging business or food establishment, e.g. from national associations or standards bodies. Use the author property to indicate the rating organization, e.g. as an Organization with name such as (e.g. HOTREC, DEHOGA, WHR, or Hotelstars).",
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
    checkinTime: Optional[
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
        description="The earliest someone may check into a lodging establishment.",
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


if TYPE_CHECKING:
    from pydantic2_schemaorg.Audience import Audience
    from pydantic2_schemaorg.Text import Text
    from pydantic2_schemaorg.Language import Language
    from pydantic2_schemaorg.DateTime import DateTime
    from pydantic2_schemaorg.Time import Time
    from pydantic2_schemaorg.Rating import Rating
    from pydantic2_schemaorg.Boolean import Boolean
    from pydantic2_schemaorg.LocationFeatureSpecification import (
        LocationFeatureSpecification,
    )
    from pydantic2_schemaorg.Number import Number
    from pydantic2_schemaorg.QuantitativeValue import QuantitativeValue
