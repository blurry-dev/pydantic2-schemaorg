from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class CausesHealthAspect(HealthAspectEnumeration):
    """Information about the causes and main actions that gave rise to the topic.

    See: https://schema.org/CausesHealthAspect
    Model depth: 5
    """

    type_: str = Field(default="CausesHealthAspect", alias="@type", const=True)
