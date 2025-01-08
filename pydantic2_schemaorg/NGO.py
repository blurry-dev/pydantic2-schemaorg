from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Organization import Organization


class NGO(Organization):
    """Organization: Non-governmental Organization.

    See: https://schema.org/NGO
    Model depth: 3
    """

    type_: str = Field(default="NGO", alias="@type", const=True)
