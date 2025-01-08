from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalSignOrSymptom import MedicalSignOrSymptom


class MedicalSymptom(MedicalSignOrSymptom):
    """Any complaint sensed and expressed by the patient (therefore defined as subjective) like stomachache, lower-back
     pain, or fatigue.

    See: https://schema.org/MedicalSymptom
    Model depth: 5
    """

    type_: str = Field(default="MedicalSymptom", alias="@type", const=True)
