from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.RestrictedDiet import RestrictedDiet


class DiabeticDiet(RestrictedDiet):
    """A diet appropriate for people with diabetes.

    See: https://schema.org/DiabeticDiet
    Model depth: 5
    """

    type_: str = Field(default="DiabeticDiet", alias="@type", const=True)
