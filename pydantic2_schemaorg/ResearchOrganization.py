from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Organization import Organization


class ResearchOrganization(Organization):
    """A Research Organization (e.g. scientific institute, research company).

    See: https://schema.org/ResearchOrganization
    Model depth: 3
    """

    type_: str = Field(default="ResearchOrganization", alias="@type", const=True)
