from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class OverviewHealthAspect(HealthAspectEnumeration):
    """Overview of the content. Contains a summarized view of the topic with the most relevant information for an
     introduction.

    See: https://schema.org/OverviewHealthAspect
    Model depth: 5
    """

    type_: str = Field(default="OverviewHealthAspect", alias="@type", const=True)
