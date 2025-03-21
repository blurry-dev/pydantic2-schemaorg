from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class StagesHealthAspect(HealthAspectEnumeration):
    """Stages that can be observed from a topic.

    See: https://schema.org/StagesHealthAspect
    Model depth: 5
    """

    type_: str = Field(default="StagesHealthAspect", alias="@type", const=True)
