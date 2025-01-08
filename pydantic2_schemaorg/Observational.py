from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalObservationalStudyDesign import (
    MedicalObservationalStudyDesign,
)


class Observational(MedicalObservationalStudyDesign):
    """An observational study design.

    See: https://schema.org/Observational
    Model depth: 6
    """

    type_: str = Field(default="Observational", alias="@type", const=True)
