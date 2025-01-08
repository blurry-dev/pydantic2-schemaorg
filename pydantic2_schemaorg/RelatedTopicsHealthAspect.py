from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class RelatedTopicsHealthAspect(HealthAspectEnumeration):
    """Other prominent or relevant topics tied to the main topic.

    See: https://schema.org/RelatedTopicsHealthAspect
    Model depth: 5
    """

    type_: str = Field(default="RelatedTopicsHealthAspect", alias="@type", const=True)
