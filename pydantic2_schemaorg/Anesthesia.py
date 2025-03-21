from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalSpecialty import MedicalSpecialty


class Anesthesia(MedicalSpecialty):
    """A specific branch of medical science that pertains to study of anesthetics and their application.

    See: https://schema.org/Anesthesia
    Model depth: 6
    """

    type_: str = Field(default="Anesthesia", alias="@type", const=True)
