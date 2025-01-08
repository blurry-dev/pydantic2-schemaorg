from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalSpecialty import MedicalSpecialty
from pydantic2_schemaorg.MedicalBusiness import MedicalBusiness


class Dermatology(MedicalSpecialty, MedicalBusiness):
    """A specific branch of medical science that pertains to diagnosis and treatment of disorders of skin.

    See: https://schema.org/Dermatology
    Model depth: 5
    """

    type_: str = Field(default="Dermatology", alias="@type", const=True)
