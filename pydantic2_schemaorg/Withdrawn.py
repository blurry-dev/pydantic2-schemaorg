from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalStudyStatus import MedicalStudyStatus


class Withdrawn(MedicalStudyStatus):
    """Withdrawn.

    See: https://schema.org/Withdrawn
    Model depth: 6
    """

    type_: str = Field(default="Withdrawn", alias="@type", const=True)
