from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalImagingTechnique import MedicalImagingTechnique


class MRI(MedicalImagingTechnique):
    """Magnetic resonance imaging.

    See: https://schema.org/MRI
    Model depth: 6
    """

    type_: str = Field(default="MRI", alias="@type", const=True)
