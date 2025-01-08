from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalSpecialty import MedicalSpecialty
from pydantic2_schemaorg.MedicalBusiness import MedicalBusiness


class Podiatric(MedicalSpecialty, MedicalBusiness):
    """Podiatry is the care of the human foot, especially the diagnosis and treatment of foot disorders.

    See: https://schema.org/Podiatric
    Model depth: 5
    """

    type_: str = Field(default="Podiatric", alias="@type", const=True)
