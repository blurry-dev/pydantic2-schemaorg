from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalSpecialty import MedicalSpecialty
from pydantic2_schemaorg.MedicalBusiness import MedicalBusiness


class Nursing(MedicalSpecialty, MedicalBusiness):
    """A health profession of a person formally educated and trained in the care of the sick or infirm person.

    See: https://schema.org/Nursing
    Model depth: 5
    """

    type_: str = Field(default="Nursing", alias="@type", const=True)
