from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalSpecialty import MedicalSpecialty


class Gastroenterologic(MedicalSpecialty):
    """A specific branch of medical science that pertains to diagnosis and treatment of disorders of digestive system.

    See: https://schema.org/Gastroenterologic
    Model depth: 6
    """

    type_: str = Field(default="Gastroenterologic", alias="@type", const=True)
