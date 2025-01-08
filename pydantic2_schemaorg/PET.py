from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalImagingTechnique import MedicalImagingTechnique


class PET(MedicalImagingTechnique):
    """Positron emission tomography imaging.

    See: https://schema.org/PET
    Model depth: 6
    """

    type_: str = Field(default="PET", alias="@type", const=True)
