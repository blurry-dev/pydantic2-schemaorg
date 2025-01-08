from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.MedicalObservationalStudyDesign import (
    MedicalObservationalStudyDesign,
)


class Registry(MedicalObservationalStudyDesign):
    """A registry-based study design.

    See: https://schema.org/Registry
    Model depth: 6
    """

    type_: str = Field(default="Registry", alias="@type", const=True)
