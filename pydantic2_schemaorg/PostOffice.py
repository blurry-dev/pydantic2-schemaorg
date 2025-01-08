from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.GovernmentOffice import GovernmentOffice


class PostOffice(GovernmentOffice):
    """A post office.

    See: https://schema.org/PostOffice
    Model depth: 5
    """

    type_: str = Field(default="PostOffice", alias="@type", const=True)
