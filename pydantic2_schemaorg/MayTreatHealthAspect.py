from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class MayTreatHealthAspect(HealthAspectEnumeration):
    """Related topics may be treated by a Topic.

    See: https://schema.org/MayTreatHealthAspect
    Model depth: 5
    """

    type_: str = Field(default="MayTreatHealthAspect", alias="@type", const=True)
