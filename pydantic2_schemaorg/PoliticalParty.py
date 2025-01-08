from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Organization import Organization


class PoliticalParty(Organization):
    """Organization: Political Party.

    See: https://schema.org/PoliticalParty
    Model depth: 3
    """

    type_: str = Field(default="PoliticalParty", alias="@type", const=True)
