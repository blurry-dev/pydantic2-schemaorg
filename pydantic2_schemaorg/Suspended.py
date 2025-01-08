from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalStudyStatus import MedicalStudyStatus


class Suspended(MedicalStudyStatus):
    """Suspended.

    See: https://schema.org/Suspended
    Model depth: 6
    """

    type_: str = Field(default="Suspended", alias="@type", const=True)
