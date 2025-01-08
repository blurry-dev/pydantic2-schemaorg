from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalEnumeration import MedicalEnumeration


class MedicineSystem(MedicalEnumeration):
    """Systems of medical practice.

    See: https://schema.org/MedicineSystem
    Model depth: 5
    """

    type_: str = Field(default="MedicineSystem", alias="@type", const=True)
