from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalEvidenceLevel import MedicalEvidenceLevel


class EvidenceLevelC(MedicalEvidenceLevel):
    """Only consensus opinion of experts, case studies, or standard-of-care.

    See: https://schema.org/EvidenceLevelC
    Model depth: 6
    """

    type_: str = Field(default="EvidenceLevelC", alias="@type", const=True)
