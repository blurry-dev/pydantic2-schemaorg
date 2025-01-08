from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalImagingTechnique import MedicalImagingTechnique
from pydantic2_schemaorg.MedicalSpecialty import MedicalSpecialty


class Radiography(MedicalImagingTechnique, MedicalSpecialty):
    """Radiography is an imaging technique that uses electromagnetic radiation other than visible light, especially
     X-rays, to view the internal structure of a non-uniformly composed and opaque object such as the human body.

    See: https://schema.org/Radiography
    Model depth: 6
    """

    type_: str = Field(default="Radiography", alias="@type", const=True)
