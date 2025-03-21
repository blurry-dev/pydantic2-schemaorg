from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class SymptomsHealthAspect(HealthAspectEnumeration):
    """Symptoms or related symptoms of a Topic.

    See: https://schema.org/SymptomsHealthAspect
    Model depth: 5
    """

    type_: str = Field(default="SymptomsHealthAspect", alias="@type", const=True)
