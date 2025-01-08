from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalTherapy import MedicalTherapy


class RadiationTherapy(MedicalTherapy):
    """A process of care using radiation aimed at improving a health condition.

    See: https://schema.org/RadiationTherapy
    Model depth: 6
    """

    type_: str = Field(default="RadiationTherapy", alias="@type", const=True)
