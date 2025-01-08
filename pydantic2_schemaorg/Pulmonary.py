from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalSpecialty import MedicalSpecialty


class Pulmonary(MedicalSpecialty):
    """A specific branch of medical science that pertains to the study of the respiratory system and its respective
     disease states.

    See: https://schema.org/Pulmonary
    Model depth: 6
    """

    type_: str = Field(default="Pulmonary", alias="@type", const=True)
