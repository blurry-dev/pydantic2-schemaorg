from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class TreatmentsHealthAspect(HealthAspectEnumeration):
    """Treatments or related therapies for a Topic.

    See: https://schema.org/TreatmentsHealthAspect
    Model depth: 5
    """

    type_: str = Field(default="TreatmentsHealthAspect", alias="@type", const=True)
