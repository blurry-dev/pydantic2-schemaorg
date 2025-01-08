from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class MisconceptionsHealthAspect(HealthAspectEnumeration):
    """Content about common misconceptions and myths that are related to a topic.

    See: https://schema.org/MisconceptionsHealthAspect
    Model depth: 5
    """

    type_: str = Field(default="MisconceptionsHealthAspect", alias="@type", const=True)
