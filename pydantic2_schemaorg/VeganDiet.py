from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.RestrictedDiet import RestrictedDiet


class VeganDiet(RestrictedDiet):
    """A diet exclusive of all animal products.

    See: https://schema.org/VeganDiet
    Model depth: 5
    """

    type_: str = Field(default="VeganDiet", alias="@type", const=True)
