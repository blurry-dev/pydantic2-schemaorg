from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.RestrictedDiet import RestrictedDiet


class LowSaltDiet(RestrictedDiet):
    """A diet focused on reduced sodium intake.

    See: https://schema.org/LowSaltDiet
    Model depth: 5
    """

    type_: str = Field(default="LowSaltDiet", alias="@type", const=True)
