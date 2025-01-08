from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class PrognosisHealthAspect(HealthAspectEnumeration):
    """Typical progression and happenings of life course of the topic.

    See: https://schema.org/PrognosisHealthAspect
    Model depth: 5
    """

    type_: str = Field(default="PrognosisHealthAspect", alias="@type", const=True)
