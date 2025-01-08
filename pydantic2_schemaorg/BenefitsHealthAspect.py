from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class BenefitsHealthAspect(HealthAspectEnumeration):
    """Content about the benefits and advantages of usage or utilization of topic.

    See: https://schema.org/BenefitsHealthAspect
    Model depth: 5
    """

    type_: str = Field(default="BenefitsHealthAspect", alias="@type", const=True)
