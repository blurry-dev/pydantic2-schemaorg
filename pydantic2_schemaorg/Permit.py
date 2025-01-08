from __future__ import annotations
from typing import TYPE_CHECKING

from datetime import date, datetime
from typing import List, Optional, Union


from pydantic.v1 import Field
from pydantic2_schemaorg.Intangible import Intangible


class Permit(Intangible):
    """A permit issued by an organization, e.g. a parking pass.

    See: https://schema.org/Permit
    Model depth: 3
    """

    type_: str = Field(default="Permit", alias="@type", const=True)
    validUntil: Optional[Union[List[Union[date, "Date", str]], date, "Date", str]] = (
        Field(
            default=None,
            description="The date when the item is no longer valid.",
        )
    )
    validIn: Optional[
        Union[List[Union["AdministrativeArea", str]], "AdministrativeArea", str]
    ] = Field(
        default=None,
        description="The geographic area where the item is valid. Applies for example to a [[Permit]], a [[Certification]], or an [[EducationalOccupationalCredential]].",
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
    issuedThrough: Optional[Union[List[Union["Service", str]], "Service", str]] = Field(
        default=None,
        description="The service through which the permit was granted.",
    )
    issuedBy: Optional[Union[List[Union["Organization", str]], "Organization", str]] = (
        Field(
            default=None,
            description="The organization issuing the item, for example a [[Permit]], [[Ticket]], or [[Certification]].",
        )
    )
    permitAudience: Optional[Union[List[Union["Audience", str]], "Audience", str]] = (
        Field(
            default=None,
            description="The target audience for this permit.",
        )
    )
    validFor: Optional[Union[List[Union["Duration", str]], "Duration", str]] = Field(
        default=None,
        description="The duration of validity of a permit or similar thing.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.Date import Date
    from pydantic2_schemaorg.AdministrativeArea import AdministrativeArea
    from pydantic2_schemaorg.DateTime import DateTime
    from pydantic2_schemaorg.Service import Service
    from pydantic2_schemaorg.Organization import Organization
    from pydantic2_schemaorg.Audience import Audience
    from pydantic2_schemaorg.Duration import Duration
