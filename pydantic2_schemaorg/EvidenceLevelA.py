from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalEvidenceLevel import MedicalEvidenceLevel


class EvidenceLevelA(MedicalEvidenceLevel):
    """Data derived from multiple randomized clinical trials or meta-analyses.

    See: https://schema.org/EvidenceLevelA
    Model depth: 6
    """

    type_: str = Field(default="EvidenceLevelA", alias="@type", const=True)
