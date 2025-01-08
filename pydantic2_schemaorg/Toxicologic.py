from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalSpecialty import MedicalSpecialty


class Toxicologic(MedicalSpecialty):
    """A specific branch of medical science that is concerned with poisons, their nature, effects and detection
     and involved in the treatment of poisoning.

    See: https://schema.org/Toxicologic
    Model depth: 6
    """

    type_: str = Field(default="Toxicologic", alias="@type", const=True)
