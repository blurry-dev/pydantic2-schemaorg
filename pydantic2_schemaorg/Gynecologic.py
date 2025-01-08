from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalSpecialty import MedicalSpecialty
from pydantic2_schemaorg.MedicalBusiness import MedicalBusiness


class Gynecologic(MedicalSpecialty, MedicalBusiness):
    """A specific branch of medical science that pertains to the health care of women, particularly in the diagnosis
     and treatment of disorders affecting the female reproductive system.

    See: https://schema.org/Gynecologic
    Model depth: 5
    """

    type_: str = Field(default="Gynecologic", alias="@type", const=True)
