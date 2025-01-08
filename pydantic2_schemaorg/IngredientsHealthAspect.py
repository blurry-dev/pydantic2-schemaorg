from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class IngredientsHealthAspect(HealthAspectEnumeration):
    """Content discussing ingredients-related aspects of a health topic.

    See: https://schema.org/IngredientsHealthAspect
    Model depth: 5
    """

    type_: str = Field(default="IngredientsHealthAspect", alias="@type", const=True)
