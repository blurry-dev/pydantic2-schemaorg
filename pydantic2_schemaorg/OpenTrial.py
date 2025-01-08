from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalTrialDesign import MedicalTrialDesign


class OpenTrial(MedicalTrialDesign):
    """A trial design in which the researcher knows the full details of the treatment, and so does the patient.

    See: https://schema.org/OpenTrial
    Model depth: 6
    """

    type_: str = Field(default="OpenTrial", alias="@type", const=True)
