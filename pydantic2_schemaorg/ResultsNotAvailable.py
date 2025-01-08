from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalStudyStatus import MedicalStudyStatus


class ResultsNotAvailable(MedicalStudyStatus):
    """Results are not available.

    See: https://schema.org/ResultsNotAvailable
    Model depth: 6
    """

    type_: str = Field(default="ResultsNotAvailable", alias="@type", const=True)
