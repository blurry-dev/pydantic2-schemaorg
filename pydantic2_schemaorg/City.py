from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.AdministrativeArea import AdministrativeArea


class City(AdministrativeArea):
    """A city or town.

    See: https://schema.org/City
    Model depth: 4
    """

    type_: str = Field(default="City", alias="@type", const=True)
