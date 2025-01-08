from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalStudyStatus import MedicalStudyStatus


class EnrollingByInvitation(MedicalStudyStatus):
    """Enrolling participants by invitation only.

    See: https://schema.org/EnrollingByInvitation
    Model depth: 6
    """

    type_: str = Field(default="EnrollingByInvitation", alias="@type", const=True)
