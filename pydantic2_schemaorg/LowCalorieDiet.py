from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.RestrictedDiet import RestrictedDiet


class LowCalorieDiet(RestrictedDiet):
    """A diet focused on reduced calorie intake.

    See: https://schema.org/LowCalorieDiet
    Model depth: 5
    """

    type_: str = Field(default="LowCalorieDiet", alias="@type", const=True)
