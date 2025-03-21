from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalEntity import MedicalEntity


class MedicalStudy(MedicalEntity):
    """A medical study is an umbrella type covering all kinds of research studies relating to human medicine or health,
     including observational studies and interventional trials and registries, randomized, controlled or
     not. When the specific type of study is known, use one of the extensions of this type, such as MedicalTrial or
     MedicalObservationalStudy. Also, note that this type should be used to mark up data that describes the study
     itself; to tag an article that publishes the results of a study, use MedicalScholarlyArticle. Note: use the
     code property of MedicalEntity to store study IDs, e.g. clinicaltrials.gov ID.

    See: https://schema.org/MedicalStudy
    Model depth: 3
    """

    type_: str = Field(default="MedicalStudy", alias="@type", const=True)
    healthCondition: Optional[
        Union[List[Union["MedicalCondition", str]], "MedicalCondition", str]
    ] = Field(
        default=None,
        description="Specifying the health condition(s) of a patient, medical study, or other target audience.",
    )
    studyLocation: Optional[
        Union[List[Union["AdministrativeArea", str]], "AdministrativeArea", str]
    ] = Field(
        default=None,
        description="The location in which the study is taking/took place.",
    )
    sponsor: Optional[
        Union[List[Union["Person", "Organization", str]], "Person", "Organization", str]
    ] = Field(
        default=None,
        description="A person or organization that supports a thing through a pledge, promise, or financial contribution. E.g. a sponsor of a Medical Study or a corporate sponsor of an event.",
    )
    studySubject: Optional[
        Union[List[Union["MedicalEntity", str]], "MedicalEntity", str]
    ] = Field(
        default=None,
        description="A subject of the study, i.e. one of the medical conditions, therapies, devices, drugs, etc. investigated by the study.",
    )
    status: Optional[
        Union[
            List[Union[str, "Text", "EventStatusType", "MedicalStudyStatus"]],
            str,
            "Text",
            "EventStatusType",
            "MedicalStudyStatus",
        ]
    ] = Field(
        default=None,
        description="The status of the study (enumerated).",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.MedicalCondition import MedicalCondition
    from pydantic2_schemaorg.AdministrativeArea import AdministrativeArea
    from pydantic2_schemaorg.Person import Person
    from pydantic2_schemaorg.Organization import Organization
    from pydantic2_schemaorg.MedicalEntity import MedicalEntity
    from pydantic2_schemaorg.Text import Text
    from pydantic2_schemaorg.EventStatusType import EventStatusType
    from pydantic2_schemaorg.MedicalStudyStatus import MedicalStudyStatus
