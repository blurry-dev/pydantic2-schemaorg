from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.DoseSchedule import DoseSchedule


class ReportedDoseSchedule(DoseSchedule):
    """A patient-reported or observed dosing schedule for a drug or supplement.

    See: https://schema.org/ReportedDoseSchedule
    Model depth: 5
    """

    type_: str = Field(default="ReportedDoseSchedule", alias="@type", const=True)
