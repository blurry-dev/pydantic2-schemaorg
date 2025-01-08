from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from pydantic.v1 import AnyUrl, StrictBool
from datetime import date, datetime, time


from pydantic.v1 import Field
from pydantic2_schemaorg.Intangible import Intangible


class ActionAccessSpecification(Intangible):
    """A set of requirements that must be fulfilled in order to perform an Action.

    See: https://schema.org/ActionAccessSpecification
    Model depth: 3
    """

    type_: str = Field(default="ActionAccessSpecification", alias="@type", const=True)
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
    expectsAcceptanceOf: Optional[Union[List[Union["Offer", str]], "Offer", str]] = (
        Field(
            default=None,
            description="An Offer which must be accepted before the user can perform the Action. For example, the user may need to buy a movie before being able to watch it.",
        )
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
    requiresSubscription: Optional[
        Union[
            List[Union[StrictBool, "Boolean", "MediaSubscription", str]],
            StrictBool,
            "Boolean",
            "MediaSubscription",
            str,
        ]
    ] = Field(
        default=None,
        description="Indicates if use of the media require a subscription (either paid or free). Allowed values are ```true``` or ```false``` (note that an earlier version had 'yes', 'no').",
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


if TYPE_CHECKING:
    from pydantic2_schemaorg.Text import Text
    from pydantic2_schemaorg.Place import Place
    from pydantic2_schemaorg.GeoShape import GeoShape
    from pydantic2_schemaorg.URL import URL
    from pydantic2_schemaorg.PhysicalActivityCategory import PhysicalActivityCategory
    from pydantic2_schemaorg.CategoryCode import CategoryCode
    from pydantic2_schemaorg.Thing import Thing
    from pydantic2_schemaorg.DateTime import DateTime
    from pydantic2_schemaorg.Time import Time
    from pydantic2_schemaorg.Date import Date
    from pydantic2_schemaorg.Offer import Offer
    from pydantic2_schemaorg.Boolean import Boolean
    from pydantic2_schemaorg.MediaSubscription import MediaSubscription
