from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalSpecialty import MedicalSpecialty
from pydantic2_schemaorg.MedicalBusiness import MedicalBusiness


class CommunityHealth(MedicalSpecialty, MedicalBusiness):
    """A field of public health focusing on improving health characteristics of a defined population in relation
     with their geographical or environment areas.

    See: https://schema.org/CommunityHealth
    Model depth: 5
    """

    type_: str = Field(default="CommunityHealth", alias="@type", const=True)
