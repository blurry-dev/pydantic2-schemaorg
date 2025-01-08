from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalTrialDesign import MedicalTrialDesign


class SingleCenterTrial(MedicalTrialDesign):
    """A trial that takes place at a single center.

    See: https://schema.org/SingleCenterTrial
    Model depth: 6
    """

    type_: str = Field(default="SingleCenterTrial", alias="@type", const=True)
