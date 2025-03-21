from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.RestrictedDiet import RestrictedDiet


class HinduDiet(RestrictedDiet):
    """A diet conforming to Hindu dietary practices, in particular, beef-free.

    See: https://schema.org/HinduDiet
    Model depth: 5
    """

    type_: str = Field(default="HinduDiet", alias="@type", const=True)
