from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalTrialDesign import MedicalTrialDesign


class MultiCenterTrial(MedicalTrialDesign):
    """A trial that takes place at multiple centers.

    See: https://schema.org/MultiCenterTrial
    Model depth: 6
    """

    type_: str = Field(default="MultiCenterTrial", alias="@type", const=True)
