from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalEnumeration import MedicalEnumeration


class MedicalTrialDesign(MedicalEnumeration):
    """Design models for medical trials. Enumerated type.

    See: https://schema.org/MedicalTrialDesign
    Model depth: 5
    """

    type_: str = Field(default="MedicalTrialDesign", alias="@type", const=True)
