from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalStudyStatus import MedicalStudyStatus


class Completed(MedicalStudyStatus):
    """Completed.

    See: https://schema.org/Completed
    Model depth: 6
    """

    type_: str = Field(default="Completed", alias="@type", const=True)
