from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Organization import Organization


class SearchRescueOrganization(Organization):
    """A Search and Rescue organization of some kind.

    See: https://schema.org/SearchRescueOrganization
    Model depth: 3
    """

    type_: str = Field(default="SearchRescueOrganization", alias="@type", const=True)
