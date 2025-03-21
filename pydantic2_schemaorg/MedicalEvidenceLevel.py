from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalEnumeration import MedicalEnumeration


class MedicalEvidenceLevel(MedicalEnumeration):
    """Level of evidence for a medical guideline. Enumerated type.

    See: https://schema.org/MedicalEvidenceLevel
    Model depth: 5
    """

    type_: str = Field(default="MedicalEvidenceLevel", alias="@type", const=True)
