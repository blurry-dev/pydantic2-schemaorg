from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalEntity import MedicalEntity


class LifestyleModification(MedicalEntity):
    """A process of care involving exercise, changes to diet, fitness routines, and other lifestyle changes aimed
     at improving a health condition.

    See: https://schema.org/LifestyleModification
    Model depth: 3
    """

    type_: str = Field(default="LifestyleModification", alias="@type", const=True)
