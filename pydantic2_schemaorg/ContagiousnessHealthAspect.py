from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class ContagiousnessHealthAspect(HealthAspectEnumeration):
    """Content about contagion mechanisms and contagiousness information over the topic.

    See: https://schema.org/ContagiousnessHealthAspect
    Model depth: 5
    """

    type_: str = Field(default="ContagiousnessHealthAspect", alias="@type", const=True)
