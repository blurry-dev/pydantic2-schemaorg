from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalTrialDesign import MedicalTrialDesign


class DoubleBlindedTrial(MedicalTrialDesign):
    """A trial design in which neither the researcher nor the patient knows the details of the treatment the patient
     was randomly assigned to.

    See: https://schema.org/DoubleBlindedTrial
    Model depth: 6
    """

    type_: str = Field(default="DoubleBlindedTrial", alias="@type", const=True)
