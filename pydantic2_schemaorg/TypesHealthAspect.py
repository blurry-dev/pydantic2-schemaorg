from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class TypesHealthAspect(HealthAspectEnumeration):
    """Categorization and other types related to a topic.

    See: https://schema.org/TypesHealthAspect
    Model depth: 5
    """

    type_: str = Field(default="TypesHealthAspect", alias="@type", const=True)
