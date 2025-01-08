from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalSpecialty import MedicalSpecialty
from pydantic2_schemaorg.MedicalBusiness import MedicalBusiness


class Psychiatric(MedicalSpecialty, MedicalBusiness):
    """A specific branch of medical science that is concerned with the study, treatment, and prevention of mental
     illness, using both medical and psychological therapies.

    See: https://schema.org/Psychiatric
    Model depth: 5
    """

    type_: str = Field(default="Psychiatric", alias="@type", const=True)
