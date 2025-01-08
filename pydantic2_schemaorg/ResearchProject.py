from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Project import Project


class ResearchProject(Project):
    """A Research project.

    See: https://schema.org/ResearchProject
    Model depth: 4
    """

    type_: str = Field(default="ResearchProject", alias="@type", const=True)
