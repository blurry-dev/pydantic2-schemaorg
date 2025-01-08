from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.RestrictedDiet import RestrictedDiet


class LowFatDiet(RestrictedDiet):
    """A diet focused on reduced fat and cholesterol intake.

    See: https://schema.org/LowFatDiet
    Model depth: 5
    """

    type_: str = Field(default="LowFatDiet", alias="@type", const=True)
