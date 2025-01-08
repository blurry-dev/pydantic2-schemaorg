from __future__ import annotations
from typing import TYPE_CHECKING

from datetime import date, datetime
from typing import List, Optional, Union
from pydantic.v1 import AnyUrl


from pydantic.v1 import Field
from pydantic2_schemaorg.CreativeWork import CreativeWork


class Certification(CreativeWork):
    """A Certification is an official and authoritative statement about a subject, for example a product, service,
     person, or organization. A certification is typically issued by an indendent certification body, for example
     a professional organization or government. It formally attests certain characteristics about the subject,
     for example Organizations can be ISO certified, Food products can be certified Organic or Vegan, a Person
     can be a certified professional, a Place can be certified for food processing. There are certifications for
     many domains: regulatory, organizational, recycling, food, efficiency, educational, ecological, etc.
     A certification is a form of credential, as are accreditations and licenses. Mapped from the [gs1:CertificationDetails](https://www.gs1.org/voc/CertificationDetails)
     class in the GS1 Web Vocabulary.

    See: https://schema.org/Certification
    Model depth: 3
    """

    type_: str = Field(default="Certification", alias="@type", const=True)
    datePublished: Optional[
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
        description="Date of first publication or broadcast. For example the date a [[CreativeWork]] was broadcast or a [[Certification]] was issued.",
    )
    auditDate: Optional[
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
        description="Date when a certification was last audited. See also [gs1:certificationAuditDate](https://www.gs1.org/voc/certificationAuditDate).",
    )
    certificationRating: Optional[Union[List[Union["Rating", str]], "Rating", str]] = (
        Field(
            default=None,
            description="Rating of a certification instance (as defined by an independent certification body). Typically this rating can be used to rate the level to which the requirements of the certification instance are fulfilled. See also [gs1:certificationValue](https://www.gs1.org/voc/certificationValue).",
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
    certificationIdentification: Optional[
        Union[List[Union[str, "Text", "DefinedTerm"]], str, "Text", "DefinedTerm"]
    ] = Field(
        default=None,
        description="Identifier of a certification instance (as registered with an independent certification body). Typically this identifier can be used to consult and verify the certification instance. See also [gs1:certificationIdentification](https://www.gs1.org/voc/certificationIdentification).",
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
    about: Optional[Union[List[Union["Thing", str]], "Thing", str]] = Field(
        default=None,
        description="The subject matter of the content.",
    )
    hasMeasurement: Optional[
        Union[List[Union["QuantitativeValue", str]], "QuantitativeValue", str]
    ] = Field(
        default=None,
        description="A measurement of an item, For example, the inseam of pants, the wheel size of a bicycle, the gauge of a screw, or the carbon footprint measured for certification by an authority. Usually an exact measurement, but can also be a range of measurements for adjustable products, for example belts and ski bindings.",
    )
    issuedBy: Optional[Union[List[Union["Organization", str]], "Organization", str]] = (
        Field(
            default=None,
            description="The organization issuing the item, for example a [[Permit]], [[Ticket]], or [[Certification]].",
        )
    )
    certificationStatus: Optional[
        Union[
            List[Union["CertificationStatusEnumeration", str]],
            "CertificationStatusEnumeration",
            str,
        ]
    ] = Field(
        default=None,
        description="Indicates the current status of a certification: active or inactive. See also [gs1:certificationStatus](https://www.gs1.org/voc/certificationStatus).",
    )
    expires: Optional[
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
        description="Date the content expires and is no longer useful or available. For example a [[VideoObject]] or [[NewsArticle]] whose availability or relevance is time-limited, a [[ClaimReview]] fact check whose publisher wants to indicate that it may no longer be relevant (or helpful to highlight) after some date, or a [[Certification]] the validity has expired.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.DateTime import DateTime
    from pydantic2_schemaorg.Date import Date
    from pydantic2_schemaorg.Rating import Rating
    from pydantic2_schemaorg.AdministrativeArea import AdministrativeArea
    from pydantic2_schemaorg.Text import Text
    from pydantic2_schemaorg.DefinedTerm import DefinedTerm
    from pydantic2_schemaorg.URL import URL
    from pydantic2_schemaorg.ImageObject import ImageObject
    from pydantic2_schemaorg.Thing import Thing
    from pydantic2_schemaorg.QuantitativeValue import QuantitativeValue
    from pydantic2_schemaorg.Organization import Organization
    from pydantic2_schemaorg.CertificationStatusEnumeration import (
        CertificationStatusEnumeration,
    )
