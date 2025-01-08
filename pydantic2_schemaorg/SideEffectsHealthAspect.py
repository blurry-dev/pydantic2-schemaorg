from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class SideEffectsHealthAspect(HealthAspectEnumeration):
    """Side effects that can be observed from the usage of the topic.

    See: https://schema.org/SideEffectsHealthAspect
    Model depth: 5
    """

    type_: str = Field(default="SideEffectsHealthAspect", alias="@type", const=True)
