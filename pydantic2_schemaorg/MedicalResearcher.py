from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalAudienceType import MedicalAudienceType


class MedicalResearcher(MedicalAudienceType):
    """Medical researchers.

    See: https://schema.org/MedicalResearcher
    Model depth: 6
    """

    type_: str = Field(default="MedicalResearcher", alias="@type", const=True)
