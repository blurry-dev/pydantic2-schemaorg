from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalSpecialty import MedicalSpecialty
from pydantic2_schemaorg.MedicalBusiness import MedicalBusiness


class PublicHealth(MedicalSpecialty, MedicalBusiness):
    """Branch of medicine that pertains to the health services to improve and protect community health, especially
     epidemiology, sanitation, immunization, and preventive medicine.

    See: https://schema.org/PublicHealth
    Model depth: 5
    """

    type_: str = Field(default="PublicHealth", alias="@type", const=True)
