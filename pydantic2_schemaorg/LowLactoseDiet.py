from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.RestrictedDiet import RestrictedDiet


class LowLactoseDiet(RestrictedDiet):
    """A diet appropriate for people with lactose intolerance.

    See: https://schema.org/LowLactoseDiet
    Model depth: 5
    """

    type_: str = Field(default="LowLactoseDiet", alias="@type", const=True)
