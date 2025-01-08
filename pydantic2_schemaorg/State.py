from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.AdministrativeArea import AdministrativeArea


class State(AdministrativeArea):
    """A state or province of a country.

    See: https://schema.org/State
    Model depth: 4
    """

    type_: str = Field(default="State", alias="@type", const=True)
