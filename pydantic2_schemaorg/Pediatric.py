from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalSpecialty import MedicalSpecialty
from pydantic2_schemaorg.MedicalBusiness import MedicalBusiness


class Pediatric(MedicalSpecialty, MedicalBusiness):
    """A specific branch of medical science that specializes in the care of infants, children and adolescents.

    See: https://schema.org/Pediatric
    Model depth: 5
    """

    type_: str = Field(default="Pediatric", alias="@type", const=True)
