from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalStudyStatus import MedicalStudyStatus


class ResultsAvailable(MedicalStudyStatus):
    """Results are available.

    See: https://schema.org/ResultsAvailable
    Model depth: 6
    """

    type_: str = Field(default="ResultsAvailable", alias="@type", const=True)
