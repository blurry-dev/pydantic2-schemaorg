from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.RestrictedDiet import RestrictedDiet


class HalalDiet(RestrictedDiet):
    """A diet conforming to Islamic dietary practices.

    See: https://schema.org/HalalDiet
    Model depth: 5
    """

    type_: str = Field(default="HalalDiet", alias="@type", const=True)
