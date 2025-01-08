from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Landform import Landform


class Continent(Landform):
    """One of the continents (for example, Europe or Africa).

    See: https://schema.org/Continent
    Model depth: 4
    """

    type_: str = Field(default="Continent", alias="@type", const=True)
