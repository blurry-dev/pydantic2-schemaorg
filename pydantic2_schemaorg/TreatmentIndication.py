from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalIndication import MedicalIndication


class TreatmentIndication(MedicalIndication):
    """An indication for treating an underlying condition, symptom, etc.

    See: https://schema.org/TreatmentIndication
    Model depth: 4
    """

    type_: str = Field(default="TreatmentIndication", alias="@type", const=True)
