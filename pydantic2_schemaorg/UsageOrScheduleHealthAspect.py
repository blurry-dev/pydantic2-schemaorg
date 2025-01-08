from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class UsageOrScheduleHealthAspect(HealthAspectEnumeration):
    """Content about how, when, frequency and dosage of a topic.

    See: https://schema.org/UsageOrScheduleHealthAspect
    Model depth: 5
    """

    type_: str = Field(default="UsageOrScheduleHealthAspect", alias="@type", const=True)
