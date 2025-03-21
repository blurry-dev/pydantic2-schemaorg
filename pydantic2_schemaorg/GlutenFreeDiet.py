from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.RestrictedDiet import RestrictedDiet


class GlutenFreeDiet(RestrictedDiet):
    """A diet exclusive of gluten.

    See: https://schema.org/GlutenFreeDiet
    Model depth: 5
    """

    type_: str = Field(default="GlutenFreeDiet", alias="@type", const=True)
