from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class ScreeningHealthAspect(HealthAspectEnumeration):
    """Content about how to screen or further filter a topic.

    See: https://schema.org/ScreeningHealthAspect
    Model depth: 5
    """

    type_: str = Field(default="ScreeningHealthAspect", alias="@type", const=True)
