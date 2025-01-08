from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalSpecialty import MedicalSpecialty


class LaboratoryScience(MedicalSpecialty):
    """A medical science pertaining to chemical, hematological, immunologic, microscopic, or bacteriological
     diagnostic analyses or research.

    See: https://schema.org/LaboratoryScience
    Model depth: 6
    """

    type_: str = Field(default="LaboratoryScience", alias="@type", const=True)
