from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from datetime import date, datetime
from pydantic.v1 import AnyUrl, StrictInt, StrictFloat


from pydantic.v1 import Field
from pydantic2_schemaorg.Intangible import Intangible


class EducationalOccupationalProgram(Intangible):
    """A program offered by an institution which determines the learning progress to achieve an outcome, usually
     a credential like a degree or certificate. This would define a discrete set of opportunities (e.g., job, courses)
     that together constitute a program with a clear start, end, set of requirements, and transition to a new occupational
     opportunity (e.g., a job), or sometimes a higher educational opportunity (e.g., an advanced degree).

    See: https://schema.org/EducationalOccupationalProgram
    Model depth: 3
    """

    type_: str = Field(
        default="EducationalOccupationalProgram", alias="@type", const=True
    )
    programPrerequisites: Optional[
        Union[
            List[
                Union[
                    str,
                    "Text",
                    "EducationalOccupationalCredential",
                    "Course",
                    "AlignmentObject",
                ]
            ],
            str,
            "Text",
            "EducationalOccupationalCredential",
            "Course",
            "AlignmentObject",
        ]
    ] = Field(
        default=None,
        description="Prerequisites for enrolling in the program.",
    )
    endDate: Optional[
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
        description="The end date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).",
    )
    occupationalCategory: Optional[
        Union[List[Union[str, "Text", "CategoryCode"]], str, "Text", "CategoryCode"]
    ] = Field(
        default=None,
        description="A category describing the job, preferably using a term from a taxonomy such as [BLS O*NET-SOC](http://www.onetcenter.org/taxonomy.html), [ISCO-08](https://www.ilo.org/public/english/bureau/stat/isco/isco08/) or similar, with the property repeated for each applicable value. Ideally the taxonomy should be identified, and both the textual label and formal code for the category should be provided. Note: for historical reasons, any textual label and formal code provided as a literal may be assumed to be from O*NET-SOC.",
    )
    numberOfCredits: Optional[
        Union[
            List[Union[int, "Integer", "StructuredValue", str]],
            int,
            "Integer",
            "StructuredValue",
            str,
        ]
    ] = Field(
        default=None,
        description="The number of credits or units awarded by a Course or required to complete an EducationalOccupationalProgram.",
    )
    termsPerYear: Optional[
        Union[
            List[Union[StrictInt, StrictFloat, "Number", str]],
            StrictInt,
            StrictFloat,
            "Number",
            str,
        ]
    ] = Field(
        default=None,
        description="The number of times terms of study are offered per year. Semesters and quarters are common units for term. For example, if the student can only take 2 semesters for the program in one year, then termsPerYear should be 2.",
    )
    maximumEnrollment: Optional[
        Union[List[Union[int, "Integer", str]], int, "Integer", str]
    ] = Field(
        default=None,
        description="The maximum number of students who may be enrolled in the program.",
    )
    dayOfWeek: Optional[Union[List[Union["DayOfWeek", str]], "DayOfWeek", str]] = Field(
        default=None,
        description="The day of the week for which these opening hours are valid.",
    )
    educationalProgramMode: Optional[
        Union[List[Union[AnyUrl, "URL", str, "Text"]], AnyUrl, "URL", str, "Text"]
    ] = Field(
        default=None,
        description='Similar to courseMode, the medium or means of delivery of the program as a whole. The value may either be a text label (e.g. "online", "onsite" or "blended"; "synchronous" or "asynchronous"; "full-time" or "part-time") or a URL reference to a term from a controlled vocabulary (e.g. https://ceds.ed.gov/element/001311#Asynchronous ).',
    )
    typicalCreditsPerTerm: Optional[
        Union[
            List[Union[int, "Integer", "StructuredValue", str]],
            int,
            "Integer",
            "StructuredValue",
            str,
        ]
    ] = Field(
        default=None,
        description="The number of credits or units a full-time student would be expected to take in 1 term however 'term' is defined by the institution.",
    )
    termDuration: Optional[Union[List[Union["Duration", str]], "Duration", str]] = (
        Field(
            default=None,
            description="The amount of time in a term as defined by the institution. A term is a length of time where students take one or more classes. Semesters and quarters are common units for term.",
        )
    )
    financialAidEligible: Optional[
        Union[List[Union[str, "Text", "DefinedTerm"]], str, "Text", "DefinedTerm"]
    ] = Field(
        default=None,
        description="A financial aid type or program which students may use to pay for tuition or fees associated with the program.",
    )
    timeToComplete: Optional[Union[List[Union["Duration", str]], "Duration", str]] = (
        Field(
            default=None,
            description="The expected length of time to complete the program if attending full-time.",
        )
    )
    salaryUponCompletion: Optional[
        Union[
            List[Union["MonetaryAmountDistribution", str]],
            "MonetaryAmountDistribution",
            str,
        ]
    ] = Field(
        default=None,
        description="The expected salary upon completing the training.",
    )
    trainingSalary: Optional[
        Union[
            List[Union["MonetaryAmountDistribution", str]],
            "MonetaryAmountDistribution",
            str,
        ]
    ] = Field(
        default=None,
        description="The estimated salary earned while in the program.",
    )
    applicationDeadline: Optional[
        Union[List[Union[date, "Date", str]], date, "Date", str]
    ] = Field(
        default=None,
        description="The date at which the program stops collecting applications for the next enrollment cycle.",
    )
    provider: Optional[
        Union[List[Union["Person", "Organization", str]], "Person", "Organization", str]
    ] = Field(
        default=None,
        description="The service provider, service operator, or service performer; the goods producer. Another party (a seller) may offer those services or goods on behalf of the provider. A provider may also serve as the seller.",
    )
    hasCourse: Optional[Union[List[Union["Course", str]], "Course", str]] = Field(
        default=None,
        description="A course or class that is one of the learning opportunities that constitute an educational / occupational program. No information is implied about whether the course is mandatory or optional; no guarantee is implied about whether the course will be available to everyone on the program.",
    )
    programType: Optional[
        Union[List[Union[str, "Text", "DefinedTerm"]], str, "Text", "DefinedTerm"]
    ] = Field(
        default=None,
        description="The type of educational or occupational program. For example, classroom, internship, alternance, etc.",
    )
    occupationalCredentialAwarded: Optional[
        Union[
            List[
                Union[AnyUrl, "URL", str, "Text", "EducationalOccupationalCredential"]
            ],
            AnyUrl,
            "URL",
            str,
            "Text",
            "EducationalOccupationalCredential",
        ]
    ] = Field(
        default=None,
        description="A description of the qualification, award, certificate, diploma or other occupational credential awarded as a consequence of successful completion of this course or program.",
    )
    offers: Optional[
        Union[List[Union["Demand", "Offer", str]], "Demand", "Offer", str]
    ] = Field(
        default=None,
        description="An offer to provide this item&#x2014;for example, an offer to sell a product, rent the DVD of a movie, perform a service, or give away tickets to an event. Use [[businessFunction]] to indicate the kind of transaction offered, i.e. sell, lease, etc. This property can also be used to describe a [[Demand]]. While this property is listed as expected on a number of common types, it can be used in others. In that case, using a second type, such as Product or a subtype of Product, can clarify the nature of the offer.",
    )
    timeOfDay: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description='The time of day the program normally runs. For example, "evenings".',
    )
    startDate: Optional[
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
        description="The start date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).",
    )
    educationalCredentialAwarded: Optional[
        Union[
            List[
                Union[AnyUrl, "URL", str, "Text", "EducationalOccupationalCredential"]
            ],
            AnyUrl,
            "URL",
            str,
            "Text",
            "EducationalOccupationalCredential",
        ]
    ] = Field(
        default=None,
        description="A description of the qualification, award, certificate, diploma or other educational credential awarded as a consequence of successful completion of this course or program.",
    )
    applicationStartDate: Optional[
        Union[List[Union[date, "Date", str]], date, "Date", str]
    ] = Field(
        default=None,
        description="The date at which the program begins collecting applications for the next enrollment cycle.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.Text import Text
    from pydantic2_schemaorg.EducationalOccupationalCredential import (
        EducationalOccupationalCredential,
    )
    from pydantic2_schemaorg.Course import Course
    from pydantic2_schemaorg.AlignmentObject import AlignmentObject
    from pydantic2_schemaorg.DateTime import DateTime
    from pydantic2_schemaorg.Date import Date
    from pydantic2_schemaorg.CategoryCode import CategoryCode
    from pydantic2_schemaorg.Integer import Integer
    from pydantic2_schemaorg.StructuredValue import StructuredValue
    from pydantic2_schemaorg.Number import Number
    from pydantic2_schemaorg.DayOfWeek import DayOfWeek
    from pydantic2_schemaorg.URL import URL
    from pydantic2_schemaorg.Duration import Duration
    from pydantic2_schemaorg.DefinedTerm import DefinedTerm
    from pydantic2_schemaorg.MonetaryAmountDistribution import (
        MonetaryAmountDistribution,
    )
    from pydantic2_schemaorg.Person import Person
    from pydantic2_schemaorg.Organization import Organization
    from pydantic2_schemaorg.Demand import Demand
    from pydantic2_schemaorg.Offer import Offer
