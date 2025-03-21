from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalEnumeration import MedicalEnumeration


class MedicalImagingTechnique(MedicalEnumeration):
    """Any medical imaging modality typically used for diagnostic purposes. Enumerated type.

    See: https://schema.org/MedicalImagingTechnique
    Model depth: 5
    """

    type_: str = Field(default="MedicalImagingTechnique", alias="@type", const=True)
