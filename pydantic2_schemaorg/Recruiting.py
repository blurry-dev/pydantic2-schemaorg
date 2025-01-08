from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalStudyStatus import MedicalStudyStatus


class Recruiting(MedicalStudyStatus):
    """Recruiting participants.

    See: https://schema.org/Recruiting
    Model depth: 6
    """

    type_: str = Field(default="Recruiting", alias="@type", const=True)
