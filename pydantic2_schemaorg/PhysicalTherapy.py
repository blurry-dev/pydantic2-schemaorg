from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalTherapy import MedicalTherapy


class PhysicalTherapy(MedicalTherapy):
    """A process of progressive physical care and rehabilitation aimed at improving a health condition.

    See: https://schema.org/PhysicalTherapy
    Model depth: 6
    """

    type_: str = Field(default="PhysicalTherapy", alias="@type", const=True)
