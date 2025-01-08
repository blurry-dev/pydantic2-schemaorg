from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalEntity import MedicalEntity


class MedicalIntangible(MedicalEntity):
    """A utility class that serves as the umbrella for a number of 'intangible' things in the medical space.

    See: https://schema.org/MedicalIntangible
    Model depth: 3
    """

    type_: str = Field(default="MedicalIntangible", alias="@type", const=True)
