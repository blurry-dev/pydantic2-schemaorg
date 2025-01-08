from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.PhysicalActivityCategory import PhysicalActivityCategory


class StrengthTraining(PhysicalActivityCategory):
    """Physical activity that is engaged in to improve muscle and bone strength. Also referred to as resistance training.

    See: https://schema.org/StrengthTraining
    Model depth: 5
    """

    type_: str = Field(default="StrengthTraining", alias="@type", const=True)
