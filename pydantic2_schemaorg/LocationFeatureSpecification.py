from __future__ import annotations
from typing import TYPE_CHECKING

from datetime import date, datetime
from typing import List, Optional, Union


from pydantic.v1 import Field
from pydantic2_schemaorg.PropertyValue import PropertyValue


class LocationFeatureSpecification(PropertyValue):
    """Specifies a location feature by providing a structured value representing a feature of an accommodation
     as a property-value pair of varying degrees of formality.

    See: https://schema.org/LocationFeatureSpecification
    Model depth: 5
    """

    type_: str = Field(
        default="LocationFeatureSpecification", alias="@type", const=True
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
    hoursAvailable: Optional[
        Union[
            List[Union["OpeningHoursSpecification", str]],
            "OpeningHoursSpecification",
            str,
        ]
    ] = Field(
        default=None,
        description="The hours during which this service or contact is available.",
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


if TYPE_CHECKING:
    from pydantic2_schemaorg.DateTime import DateTime
    from pydantic2_schemaorg.Date import Date
    from pydantic2_schemaorg.OpeningHoursSpecification import OpeningHoursSpecification
