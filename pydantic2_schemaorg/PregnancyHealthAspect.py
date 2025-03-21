from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class PregnancyHealthAspect(HealthAspectEnumeration):
    """Content discussing pregnancy-related aspects of a health topic.

    See: https://schema.org/PregnancyHealthAspect
    Model depth: 5
    """

    type_: str = Field(default="PregnancyHealthAspect", alias="@type", const=True)
