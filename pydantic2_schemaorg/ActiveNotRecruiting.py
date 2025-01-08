from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalStudyStatus import MedicalStudyStatus


class ActiveNotRecruiting(MedicalStudyStatus):
    """Active, but not recruiting new participants.

    See: https://schema.org/ActiveNotRecruiting
    Model depth: 6
    """

    type_: str = Field(default="ActiveNotRecruiting", alias="@type", const=True)
