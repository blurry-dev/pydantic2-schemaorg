from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalTrialDesign import MedicalTrialDesign


class InternationalTrial(MedicalTrialDesign):
    """An international trial.

    See: https://schema.org/InternationalTrial
    Model depth: 6
    """

    type_: str = Field(default="InternationalTrial", alias="@type", const=True)
