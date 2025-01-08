from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalTrialDesign import MedicalTrialDesign


class RandomizedTrial(MedicalTrialDesign):
    """A randomized trial design.

    See: https://schema.org/RandomizedTrial
    Model depth: 6
    """

    type_: str = Field(default="RandomizedTrial", alias="@type", const=True)
