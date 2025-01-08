from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class LivingWithHealthAspect(HealthAspectEnumeration):
    """Information about coping or life related to the topic.

    See: https://schema.org/LivingWithHealthAspect
    Model depth: 5
    """

    type_: str = Field(default="LivingWithHealthAspect", alias="@type", const=True)
