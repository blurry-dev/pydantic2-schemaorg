from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.RestrictedDiet import RestrictedDiet


class KosherDiet(RestrictedDiet):
    """A diet conforming to Jewish dietary practices.

    See: https://schema.org/KosherDiet
    Model depth: 5
    """

    type_: str = Field(default="KosherDiet", alias="@type", const=True)
