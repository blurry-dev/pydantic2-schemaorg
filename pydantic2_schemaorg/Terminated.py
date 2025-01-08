from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalStudyStatus import MedicalStudyStatus


class Terminated(MedicalStudyStatus):
    """Terminated.

    See: https://schema.org/Terminated
    Model depth: 6
    """

    type_: str = Field(default="Terminated", alias="@type", const=True)
