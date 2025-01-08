from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalEnumeration import MedicalEnumeration
from pydantic2_schemaorg.MedicalProcedure import MedicalProcedure


class PhysicalExam(MedicalEnumeration, MedicalProcedure):
    """A type of physical examination of a patient performed by a physician.

    See: https://schema.org/PhysicalExam
    Model depth: 4
    """

    type_: str = Field(default="PhysicalExam", alias="@type", const=True)
