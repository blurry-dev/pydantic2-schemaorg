from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalEnumeration import MedicalEnumeration


class DrugPrescriptionStatus(MedicalEnumeration):
    """Indicates whether this drug is available by prescription or over-the-counter.

    See: https://schema.org/DrugPrescriptionStatus
    Model depth: 5
    """

    type_: str = Field(default="DrugPrescriptionStatus", alias="@type", const=True)
