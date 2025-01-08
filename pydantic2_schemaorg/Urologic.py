from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalSpecialty import MedicalSpecialty


class Urologic(MedicalSpecialty):
    """A specific branch of medical science that is concerned with the diagnosis and treatment of diseases pertaining
     to the urinary tract and the urogenital system.

    See: https://schema.org/Urologic
    Model depth: 6
    """

    type_: str = Field(default="Urologic", alias="@type", const=True)
