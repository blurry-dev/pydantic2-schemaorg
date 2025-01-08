from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalSpecialty import MedicalSpecialty
from pydantic2_schemaorg.MedicalBusiness import MedicalBusiness


class Otolaryngologic(MedicalSpecialty, MedicalBusiness):
    """A specific branch of medical science that is concerned with the ear, nose and throat and their respective disease
     states.

    See: https://schema.org/Otolaryngologic
    Model depth: 5
    """

    type_: str = Field(default="Otolaryngologic", alias="@type", const=True)
