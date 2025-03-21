from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.RestrictedDiet import RestrictedDiet


class VegetarianDiet(RestrictedDiet):
    """A diet exclusive of animal meat.

    See: https://schema.org/VegetarianDiet
    Model depth: 5
    """

    type_: str = Field(default="VegetarianDiet", alias="@type", const=True)
