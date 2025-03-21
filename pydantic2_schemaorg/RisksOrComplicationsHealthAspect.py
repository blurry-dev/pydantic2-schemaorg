from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class RisksOrComplicationsHealthAspect(HealthAspectEnumeration):
    """Information about the risk factors and possible complications that may follow a topic.

    See: https://schema.org/RisksOrComplicationsHealthAspect
    Model depth: 5
    """

    type_: str = Field(
        default="RisksOrComplicationsHealthAspect", alias="@type", const=True
    )
