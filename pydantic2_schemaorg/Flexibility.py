from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.PhysicalActivityCategory import PhysicalActivityCategory


class Flexibility(PhysicalActivityCategory):
    """Physical activity that is engaged in to improve joint and muscle flexibility.

    See: https://schema.org/Flexibility
    Model depth: 5
    """

    type_: str = Field(default="Flexibility", alias="@type", const=True)
