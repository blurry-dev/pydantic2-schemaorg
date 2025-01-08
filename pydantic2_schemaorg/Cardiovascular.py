from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalSpecialty import MedicalSpecialty


class Cardiovascular(MedicalSpecialty):
    """A specific branch of medical science that pertains to diagnosis and treatment of disorders of heart and vasculature.

    See: https://schema.org/Cardiovascular
    Model depth: 6
    """

    type_: str = Field(default="Cardiovascular", alias="@type", const=True)
