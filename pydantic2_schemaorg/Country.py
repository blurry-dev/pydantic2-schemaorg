from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.AdministrativeArea import AdministrativeArea


class Country(AdministrativeArea):
    """A country.

    See: https://schema.org/Country
    Model depth: 4
    """

    type_: str = Field(default="Country", alias="@type", const=True)
