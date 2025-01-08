from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalSpecialty import MedicalSpecialty


class Dermatologic(MedicalSpecialty):
    """Something relating to or practicing dermatology.

    See: https://schema.org/Dermatologic
    Model depth: 6
    """

    type_: str = Field(default="Dermatologic", alias="@type", const=True)
