from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalImagingTechnique import MedicalImagingTechnique


class Ultrasound(MedicalImagingTechnique):
    """Ultrasound imaging.

    See: https://schema.org/Ultrasound
    Model depth: 6
    """

    type_: str = Field(default="Ultrasound", alias="@type", const=True)
