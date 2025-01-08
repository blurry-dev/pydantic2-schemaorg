from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalSpecialty import MedicalSpecialty
from pydantic2_schemaorg.MedicalBusiness import MedicalBusiness


class PrimaryCare(MedicalSpecialty, MedicalBusiness):
    """The medical care by a physician, or other health-care professional, who is the patient's first contact with
     the health-care system and who may recommend a specialist if necessary.

    See: https://schema.org/PrimaryCare
    Model depth: 5
    """

    type_: str = Field(default="PrimaryCare", alias="@type", const=True)
