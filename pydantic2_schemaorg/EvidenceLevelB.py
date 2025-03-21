from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalEvidenceLevel import MedicalEvidenceLevel


class EvidenceLevelB(MedicalEvidenceLevel):
    """Data derived from a single randomized trial, or nonrandomized studies.

    See: https://schema.org/EvidenceLevelB
    Model depth: 6
    """

    type_: str = Field(default="EvidenceLevelB", alias="@type", const=True)
