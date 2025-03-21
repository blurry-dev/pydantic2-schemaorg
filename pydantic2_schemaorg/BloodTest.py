from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalTest import MedicalTest


class BloodTest(MedicalTest):
    """A medical test performed on a sample of a patient's blood.

    See: https://schema.org/BloodTest
    Model depth: 4
    """

    type_: str = Field(default="BloodTest", alias="@type", const=True)
