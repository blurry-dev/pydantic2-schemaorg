from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalAudienceType import MedicalAudienceType


class Clinician(MedicalAudienceType):
    """Medical clinicians, including practicing physicians and other medical professionals involved in clinical
     practice.

    See: https://schema.org/Clinician
    Model depth: 6
    """

    type_: str = Field(default="Clinician", alias="@type", const=True)
