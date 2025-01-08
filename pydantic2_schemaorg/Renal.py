from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalSpecialty import MedicalSpecialty


class Renal(MedicalSpecialty):
    """A specific branch of medical science that pertains to the study of the kidneys and its respective disease states.

    See: https://schema.org/Renal
    Model depth: 6
    """

    type_: str = Field(default="Renal", alias="@type", const=True)
