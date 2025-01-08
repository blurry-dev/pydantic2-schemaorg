from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.PhysicalActivityCategory import PhysicalActivityCategory


class AnaerobicActivity(PhysicalActivityCategory):
    """Physical activity that is of high-intensity which utilizes the anaerobic metabolism of the body.

    See: https://schema.org/AnaerobicActivity
    Model depth: 5
    """

    type_: str = Field(default="AnaerobicActivity", alias="@type", const=True)
