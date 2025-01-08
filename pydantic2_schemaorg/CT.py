from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalImagingTechnique import MedicalImagingTechnique


class CT(MedicalImagingTechnique):
    """X-ray computed tomography imaging.

    See: https://schema.org/CT
    Model depth: 6
    """

    type_: str = Field(default="CT", alias="@type", const=True)
