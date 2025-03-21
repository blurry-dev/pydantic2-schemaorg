from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalEnumeration import MedicalEnumeration


class MedicalAudienceType(MedicalEnumeration):
    """Target audiences types for medical web pages. Enumerated type.

    See: https://schema.org/MedicalAudienceType
    Model depth: 5
    """

    type_: str = Field(default="MedicalAudienceType", alias="@type", const=True)
