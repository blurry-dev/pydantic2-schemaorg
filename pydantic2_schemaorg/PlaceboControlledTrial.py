from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalTrialDesign import MedicalTrialDesign


class PlaceboControlledTrial(MedicalTrialDesign):
    """A placebo-controlled trial design.

    See: https://schema.org/PlaceboControlledTrial
    Model depth: 6
    """

    type_: str = Field(default="PlaceboControlledTrial", alias="@type", const=True)
