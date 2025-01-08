from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalImagingTechnique import MedicalImagingTechnique


class XRay(MedicalImagingTechnique):
    """X-ray imaging.

    See: https://schema.org/XRay
    Model depth: 6
    """

    type_: str = Field(default="XRay", alias="@type", const=True)
