from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Organization import Organization


class GovernmentOrganization(Organization):
    """A governmental organization or agency.

    See: https://schema.org/GovernmentOrganization
    Model depth: 3
    """

    type_: str = Field(default="GovernmentOrganization", alias="@type", const=True)
